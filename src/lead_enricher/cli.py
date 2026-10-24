import argparse
import sys

from lead_enricher.enricher import enrich_domain


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Automated B2B company domain & contact intelligence enrichment pipeline."
    )
    parser.add_argument(
        "domains",
        nargs="*",
        default=["stripe.com", "shopify.com", "notion.so"],
        help="Company domains to enrich (defaults to sample B2B list)",
    )
    args = parser.parse_args(argv)

    print("=" * 72)
    print("   LEAD ENRICHER PRO: B2B INTELLIGENCE & CONTACT PIPELINE")
    print("=" * 72)
    print(f"[*] Processing {len(args.domains)} company domains...\n")

    for dom in args.domains:
        lead = enrich_domain(dom)
        print(f"[B2B] [{lead.company_name}] ({lead.domain}) - Fit Score: {lead.fit_score}/10")
        print(f"   Industry:    {lead.industry} | HQ: {lead.headquarters or 'N/A'}")
        print(f"   Employees:   {lead.estimated_employees} | Email: {lead.contact_email}")
        print(f"   Tech Stack:  {', '.join(lead.tech_stack)}")
        print("   Key People:")
        for person in lead.decision_makers:
            print(f"     * {person['name']} ({person['role']})")
        print()

    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
