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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides insights on customers' financial profile by evaluating bank statements, useful for digital lenders in fraud detection and underwriting.
  name: Bank Statement Analyzer API
  slug: bank-statement-analyzer-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/digitap/hosts/digitap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitap-hosts.yml
- group: other
  href: https://artifacts.apis.io/digitap/vendors/digitap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitap-vendors.yml
- group: auth
  href: https://artifacts.apis.io/digitap/security/digitap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digitap.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.digitap.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.digitap.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.digitap.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.digitap.ai/get-a-demo.html
- group: operate
  title: ''
  type: Support
  url: https://www.digitap.ai/contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://blog.digitap.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digitap
- group: start
  title: ''
  type: SignUp
  url: https://www.digitap.ai/get-a-demo.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitap.ai/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitap.ai/privacy-policy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/digitap/workspace
coverage:
  checked: '2026-10-20'
  detail: The provider's documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 404
    url: https://api.digitap.ai/openapi.json
  - status: 200
    url: https://www.digitap.ai/bank-statement-analyzer-api.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Digitap.AI provides an AI‑powered end‑to‑end API platform tailored for banking and fintech institutions. Their solutions include expense management, account aggregation, alternate data suites, onboarding, bank statement analysis, PAN verification, and mobile number verification. Founded with a vision to deliver cutting‑edge artificial intelligence and machine learning SaaS solutions, Digitap serves financial services, fintechs, and related enterprises, offering tools that automate risk management, scorecards, and data enrichment to streamline operations and improve decision‑making.
image: https://www.digitap.ai/assets/images/ai-driven-solutions.png
layout: provider
modified: '2026-10-20'
name: Digitap.AI
nav: Providers
network: true
overview: 'Digitap.AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Artificial Intelligence, and Software-as-a-Service.


  Digitap.AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 10.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Digitap Domain Security
  slug: digitap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitap
tags:
- Company
- Banking
- Fintech
- Artificial Intelligence
- Software-as-a-Service
website: https://digitap.ai/
---
