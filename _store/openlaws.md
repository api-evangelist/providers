---
aid: openlaws
name: OpenLaws
description: OpenLaws provides programmatic access to law data including statutes, regulations, and case law across U.S. jurisdictions. The API supports keyword and hybrid search, jurisdiction and court filtering, citation identification and validation, historical version queries with redline comparisons, and citation lookup with mapping to authoritative government sources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Legal
  - Law
  - Statutes
  - Regulations
  - Case Law
  - Search
  - Citations
created: '2025-03-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openlaws/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openlaws:openlaws
    name: OpenLaws
    description: OpenLaws API exposes search across statutes, regulations, and case law with BM25 or hybrid retrieval; jurisdiction and court filtering; legal citation parsing and validation; historical version queries and redline comparisons; and citation-to-government-source mapping for use in research and AI applications.
    humanURL: https://openlaws.us/api/
    baseURL: https://api.openlaws.us
    tags:
      - Legal
      - Law
      - Statutes
      - Regulations
      - Case Law
      - Search
      - Citations
    properties:
      - type: Documentation
        url: https://openlaws.apidocumentation.com
      - type: HumanURL
        url: https://openlaws.us/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
