---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Library Of Congress Agentic Access
  operation_count: 18
  slug: library-of-congress-agentic-access
  summary_line: 18 operations
api_count: 12
apis:
- description: The Bills API from Library of Congress — 3 operation(s) for bills.
  name: Library of Congress Bills API
  slug: library-of-congress-bills-api
- description: The Collections API from Library of Congress — 2 operation(s) for collections.
  name: Library of Congress Collections API
  slug: library-of-congress-collections-api
- description: The Committees API from Library of Congress — 1 operation(s) for committees.
  name: Library of Congress Committees API
  slug: library-of-congress-committees-api
- description: The Congressional Record API from Library of Congress — 1 operation(s) for congressional record.
  name: Library of Congress Congressional Record API
  slug: library-of-congress-congressional-record-api
- description: The Issues API from Library of Congress — 1 operation(s) for issues.
  name: Library of Congress Issues API
  slug: library-of-congress-issues-api
- description: The Items API from Library of Congress — 1 operation(s) for items.
  name: Library of Congress Items API
  slug: library-of-congress-items-api
- description: The Laws API from Library of Congress — 1 operation(s) for laws.
  name: Library of Congress Laws API
  slug: library-of-congress-laws-api
- description: The Members API from Library of Congress — 2 operation(s) for members.
  name: Library of Congress Members API
  slug: library-of-congress-members-api
- description: The Pages API from Library of Congress — 1 operation(s) for pages.
  name: Library of Congress Pages API
  slug: library-of-congress-pages-api
- description: The Resources API from Library of Congress — 1 operation(s) for resources.
  name: Library of Congress Resources API
  slug: library-of-congress-resources-api
- description: The Search API from Library of Congress — 1 operation(s) for search.
  name: Library of Congress Search API
  slug: library-of-congress-search-api
- description: The Titles API from Library of Congress — 3 operation(s) for titles.
  name: Library of Congress Titles API
  slug: library-of-congress-titles-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Library of Congress Chronicling America Bills API
  slug: open-library-of-congress-bills-api
- collection_type: open
  name: Library of Congress Chronicling America API
  slug: open-library-of-congress-chronicling-america-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Collections API
  slug: open-library-of-congress-collections-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Committees API
  slug: open-library-of-congress-committees-api
- collection_type: open
  name: Library of Congress Congress.gov API
  slug: open-library-of-congress-congress-gov-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Congressional Record API
  slug: open-library-of-congress-congressional-record-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Issues API
  slug: open-library-of-congress-issues-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Items API
  slug: open-library-of-congress-items-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Laws API
  slug: open-library-of-congress-laws-api
- collection_type: open
  name: Library of Congress loc.gov JSON API
  slug: open-library-of-congress-loc-gov-json-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Members API
  slug: open-library-of-congress-members-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Pages API
  slug: open-library-of-congress-pages-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Resources API
  slug: open-library-of-congress-resources-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Search API
  slug: open-library-of-congress-search-api
- collection_type: open
  name: Library of Congress Chronicling America Bills Titles API
  slug: open-library-of-congress-titles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/library-of-congress-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/library-of-congress-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/library-of-congress-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/library-of-congress-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/library-of-congress
- group: company
  title: ''
  type: Website
  url: https://www.loc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.loc.gov/apis/
- group: docs
  title: ''
  type: Reference
  url: https://www.loc.gov/apis/json-and-yaml-responses/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LibraryOfCongress
- group: company
  title: ''
  type: Blog
  url: https://blogs.loc.gov/loc/feed/
created: '2024-01-01'
description: The Library of Congress is the largest library in the world, with millions of books, films and video, audio recordings, photographs, newspapers, maps and manuscripts in its collections. The Library is the main research arm of the U.S. Congress and the home of the U.S. Copyright Office. The Library publishes a suite of public APIs that expose its catalog, digital collections, historic newspapers, and legislative information.
finops:
- name: Library Of Congress Finops
  service_category: API
  slug: library-of-congress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/library-of-congress.png
layout: provider
modified: '2026-05-19'
name: Library of Congress
nav: Providers
network: true
overview: 'Library of Congress publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Collections API, Committees API, and 9 more. Tagged areas include Cultural Heritage, Federal Government, Library, Legislative, and Newspapers.


  Library of Congress'' developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Library Of Congress Plans Pricing
  plan_count: 3
  slug: library-of-congress-plans-pricing
random_paper: 140
rate_limits:
- limit_count: 5
  name: Library Of Congress Rate Limits
  slug: library-of-congress-rate-limits
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 52.6
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/library-of-congress/refs/heads/main/screenshots/library-of-congress-2026-06-20T184501.png
security:
- kind: authentication
  name: Library Of Congress Authentication
  slug: library-of-congress-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Library Of Congress Domain Security
  slug: library-of-congress-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Library Of Congress Vulnerability Disclosure
  slug: library-of-congress-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: library-of-congress
tags:
- Cultural Heritage
- Federal Government
- Library
- Legislative
- Newspapers
- Search
website: https://www.loc.gov/
---
