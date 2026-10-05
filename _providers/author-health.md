---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation not publicly available; no machine‑readable contract found.
  name: Author Health API
  slug: author-health-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/author-health/refs/heads/main/llms/author-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/author-health-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/author-health/refs/heads/main/hosts/author-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/author-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/author-health/refs/heads/main/vendors/author-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/author-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authorhealth.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authorhealth.com/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://authorhealth.com/about/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://authorhealth.com/guides/seeking-answers
- group: company
  title: ''
  type: Blog
  url: https://authorhealth.com/blog/who-can-diagnose
- group: start
  title: ''
  type: GettingStarted
  url: https://authorhealth.com/how-it-works/virtual-care-technology-set-up-assistance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/authorhealth
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/author-health/refs/heads/main/security/author-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/author-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authorhealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Author Health provides cognitive and emotional health care services for adults, seniors, and caregivers. It offers virtual and in‑person therapy, psychiatry, and care management, focusing on conditions such as anxiety, depression, mild cognitive impairment, and dementia. The company coordinates care teams, supports insurance coverage, and delivers personalized mental health support through its online platform.
image: https://cdn.prod.website-files.com/6a1f1f50a483d33e19f6ebe5/6a32ea0e488459c1cdab6348_b85b6e30a519ca1be2164de52e19ad11_Open%20Graph.png
layout: provider
modified: '2026-09-26'
name: Author Health
nav: Providers
network: true
overview: 'Author Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mental Health, Older Adults, Medicare, Care Coordination, and Behavioral Health.


  Author Health''s developer surface includes documentation, engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Author Health Domain Security
  slug: author-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: author-health
tags:
- Mental Health
- Older Adults
- Medicare
- Care Coordination
- Behavioral Health
website: https://authorhealth.com/
---
