#!/usr/bin/env python3
"""
Setup script to create the TMT Research Notion database.

Usage:
    python scripts/setup_notion.py --parent-page-id <PAGE_ID>

Or set TMT_NOTION_PARENT_PAGE_ID in .env file.
"""

import os
import sys
import argparse
import httpx

NOTION_API_VERSION = "2022-06-28"


def create_database(notion_api_key: str, parent_page_id: str) -> dict:
    """Create the TMT Research database in Notion."""

    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json",
    }

    database_schema = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": "TMT Law Article Ideas"}}],
        "properties": {
            "Title": {
                "title": {}
            },
            "Thesis": {
                "rich_text": {}
            },
            "Category": {
                "select": {
                    "options": [
                        {"name": "Technology", "color": "blue"},
                        {"name": "Media", "color": "purple"},
                        {"name": "Telecommunications", "color": "green"},
                    ]
                }
            },
            "Legal Areas": {
                "multi_select": {
                    "options": [
                        {"name": "Data Protection", "color": "blue"},
                        {"name": "Privacy", "color": "purple"},
                        {"name": "Cybersecurity", "color": "red"},
                        {"name": "AI/ML Regulation", "color": "orange"},
                        {"name": "Platform Liability", "color": "yellow"},
                        {"name": "Content Moderation", "color": "green"},
                        {"name": "Telecom Licensing", "color": "pink"},
                        {"name": "Spectrum Policy", "color": "gray"},
                        {"name": "Broadcasting", "color": "brown"},
                        {"name": "OTT Regulation", "color": "default"},
                        {"name": "Fintech", "color": "blue"},
                        {"name": "E-commerce", "color": "purple"},
                    ]
                }
            },
            "Novel Contribution": {
                "rich_text": {}
            },
            "Key Statutes": {
                "multi_select": {
                    "options": [
                        {"name": "DPDP Act 2023", "color": "blue"},
                        {"name": "IT Act 2000", "color": "purple"},
                        {"name": "IT Rules 2021", "color": "pink"},
                        {"name": "Telecom Act 2023", "color": "green"},
                        {"name": "TRAI Act 1997", "color": "orange"},
                        {"name": "Cable TV Act 1995", "color": "yellow"},
                        {"name": "Copyright Act 1957", "color": "red"},
                        {"name": "Competition Act 2002", "color": "gray"},
                    ]
                }
            },
            "Key Cases": {
                "rich_text": {}
            },
            "Priority": {
                "select": {
                    "options": [
                        {"name": "High", "color": "red"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "Low", "color": "gray"},
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Draft", "color": "gray"},
                        {"name": "Researched", "color": "blue"},
                        {"name": "Validated", "color": "yellow"},
                        {"name": "Ready to Write", "color": "green"},
                        {"name": "Published", "color": "purple"},
                        {"name": "Rejected", "color": "red"},
                    ]
                }
            },
            "Supporting Points": {
                "rich_text": {}
            },
            "Sources": {
                "rich_text": {}
            },
            "Citation Count": {
                "number": {
                    "format": "number"
                }
            },
            "Novelty Score": {
                "number": {
                    "format": "number"
                }
            },
            "Quality Score": {
                "number": {
                    "format": "number"
                }
            },
            "Created Date": {
                "date": {}
            },
        },
    }

    with httpx.Client() as client:
        response = client.post(
            "https://api.notion.com/v1/databases",
            headers=headers,
            json=database_schema,
        )

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error creating database: {response.status_code}")
            print(response.text)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Set up TMT Research Notion database")
    parser.add_argument(
        "--parent-page-id",
        help="Notion page ID where the database will be created",
    )
    args = parser.parse_args()

    # Get API key from environment
    notion_api_key = os.getenv("TMT_NOTION_API_KEY")
    if not notion_api_key:
        print("Error: TMT_NOTION_API_KEY environment variable not set")
        print("Set it in your .env file or export it:")
        print("  export TMT_NOTION_API_KEY=secret_...")
        sys.exit(1)

    # Get parent page ID
    parent_page_id = args.parent_page_id or os.getenv("TMT_NOTION_PARENT_PAGE_ID")
    if not parent_page_id:
        print("Error: Parent page ID not provided")
        print("Either pass --parent-page-id or set TMT_NOTION_PARENT_PAGE_ID in .env")
        sys.exit(1)

    print(f"Creating TMT Research database under page: {parent_page_id}")
    result = create_database(notion_api_key, parent_page_id)

    database_id = result["id"]
    database_url = result["url"]

    print("\n✓ Database created successfully!")
    print(f"\nDatabase ID: {database_id}")
    print(f"Database URL: {database_url}")
    print(f"\nAdd this to your .env file:")
    print(f"TMT_NOTION_DATABASE_ID={database_id}")


if __name__ == "__main__":
    main()
