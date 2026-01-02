import sys
import os
import argparse
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# File to store conversation state
CONVERSATION_FILE = Path(".conversation_id")


def get_previous_response_id():
    """Load the previous response ID from file if it exists."""
    if CONVERSATION_FILE.exists():
        try:
            return CONVERSATION_FILE.read_text().strip()
        except Exception:
            return None
    return None


def save_response_id(response_id):
    """Save the response ID to file for next conversation."""
    try:
        CONVERSATION_FILE.write_text(response_id)
    except Exception as e:
        print(f"⚠️  Warning: Could not save conversation ID: {e}")


def clear_conversation():
    """Clear the conversation history."""
    if CONVERSATION_FILE.exists():
        CONVERSATION_FILE.unlink()
        print("✅ Conversation history cleared!")
    else:
        print("ℹ️  No conversation history to clear.")


def extract_response_text(response):
    """Extract text content from the response object."""
    if not response.output:
        return None
    
    text_parts = []
    for output_item in response.output:
        # Check if this is a ResponseOutputMessage (has 'content' attribute)
        if hasattr(output_item, 'content') and output_item.content:
            # Extract text from ResponseOutputMessage.content
            for content_item in output_item.content:
                if hasattr(content_item, 'text') and content_item.text:
                    text_parts.append(content_item.text)
    
    return "\n".join(text_parts) if text_parts else None


def main():
    parser = argparse.ArgumentParser(
        description="Chat with OpenAI using Responses API with conversation memory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run agi-day-1 "What's the weather in Paris?"
  uv run agi-day-1 "What did I ask you before?" --clear
  uv run agi-day-1 "Tell me more about that" --no-web-search
        """
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Your message/prompt to send to the AI"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear conversation history and start fresh"
    )
    parser.add_argument(
        "--no-web-search",
        action="store_true",
        help="Disable web search tool"
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="Model to use (default: gpt-4o-mini)"
    )
    
    args = parser.parse_args()
    
    # Handle clear conversation
    if args.clear:
        clear_conversation()
        return
    
    # Check if prompt is provided
    if not args.prompt:
        parser.print_help()
        print("\n❌ Error: Please provide a prompt!")
        print("Example: uv run agi-day-1 'What is the capital of France?'")
        sys.exit(1)
    
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n❌ Error: OPENAI_API_KEY environment variable is not set!")
        print("Please set it in your .env file or as an environment variable.")
        sys.exit(1)
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Get previous response ID for conversation continuity
    previous_response_id = get_previous_response_id()
    
    # Prepare tools
    tools = None if args.no_web_search else [{"type": "web_search_preview"}]
    
    # Make API call
    print(f"\n💬 You: {args.prompt}\n")
    print("🤖 AI: ", end="", flush=True)
    
    try:
        response = client.responses.create(
            model=args.model,
            input=args.prompt,
            store=True,
            tools=tools,
            previous_response_id=previous_response_id
        )
        
        # Save the response ID for next conversation
        save_response_id(response.id)
        
        # Extract and print the response text
        response_text = extract_response_text(response)
        
        if response_text:
            print(response_text)
            print()  # New line after response
        else:
            print("\n⚠️  No text content found in response")
            print(f"Response ID: {response.id}")
            if response.previous_response_id:
                print(f"Previous Response ID: {response.previous_response_id}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
