---
aid: unpaywall
name: Unpaywall
description: The Unpaywall REST API gives anyone free, programmatic access to the Unpaywall database of open access scholarly articles. The database covers over 120 million articles with Crossref DOIs and provides free, legal full-text links where available, with metadata on OA status (gold, hybrid, bronze, green), host type (publisher, repository), version (published, accepted, submitted), and license information.
url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
tags:
  - Open Access
  - Scholarly Articles
  - Research
  - Academic
  - Libraries
  - DOI
  - Science
apis:
  - aid: unpaywall:unpaywall
    name: Unpaywall API
    description: 'Free REST API providing open access status and full-text links for 120M+ scholarly articles. Look up any article by DOI to get its OA status, best open access location (publisher or repository), license, version, and all available free copies. Also supports title-based search across the full database. No API key required — just include your email address in requests. Rate limit: 100,000 calls per day.'
    humanURL: https://unpaywall.org/products/api
    baseURL: https://api.unpaywall.org/v2
    tags:
      - Open Access
      - DOI
      - Scholarly Articles
      - Search
    properties:
      - type: Documentation
        url: https://unpaywall.org/products/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/openapi/unpaywall-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/rules/unpaywall-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/capabilities/open-access-discovery.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/json-schema/unpaywall-article-schema.json
common:
  - type: Website
    url: https://unpaywall.org
  - type: Documentation
    url: https://unpaywall.org/products/api
  - type: DataFormat
    url: https://unpaywall.org/data-format
  - type: Support
    url: https://support.unpaywall.org
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/vocabulary/unpaywall-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/json-ld/unpaywall-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
