---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-09-19'
api_count: 2
apis:
- description: The GreyMatter API exposes select GreyMatter capabilities through a single GraphQL endpoint. All requests are HTTPS POSTs with JSON bodies authenticated by an X-API-KEY header; 58 queries and 95 mutat
  name: GreyMatter API
  slug: greymatter-api
- description: REST API of the Digital Shadows SearchLight digital-risk-protection portal, operated by ReliaQuest since its 2022 acquisition of Digital Shadows (unauthenticated calls return a JSON error that names d
  name: Digital Shadows SearchLight Portal API
  slug: searchlight-portal-api
artifact_total: 10
collections:
- collection_type: postman
  name: GreyMatter API
  slug: postman-reliaquest-greymatter-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/security/reliaquest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reliaquest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reliaquest.com/
- group: company
  title: ''
  type: Blog
  url: https://reliaquest.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://reliaquest.com/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.myreliaquest.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.myreliaquest.com/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.myreliaquest.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://reliaquest.com/product-release/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/changelog/reliaquest-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/reliaquest-changelog.yml
- group: operate
  title: ''
  type: FAQ
  url: https://reliaquest.com/resources/greymatter-faq/
- group: commercial
  title: ''
  type: Pricing
  url: https://reliaquest.com/resources/greymatter-faq/pricing-and-return-on-investment-faq/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/plans/reliaquest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reliaquest-plans-pricing.yml
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://reliaquest.com/greymatter-service-level/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reliaquest.com/greymatter-psa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reliaquest.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://reliaquest.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://reliaquest.com/about-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reliaquest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reliaquest/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://reliaquest.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/llms/reliaquest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reliaquest-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://reliaquest.com/report-potential-security-vulnerability/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://bugcrowd.com/engagements/reliaquest-vdpesf
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/packages/reliaquest-packages.yml
  title: ''
  type: Packages
  url: packages/reliaquest-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/cli/reliaquest-cli.yml
  title: ''
  type: CLI
  url: cli/reliaquest-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/conformance/reliaquest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reliaquest-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/conformance/reliaquest-conformance.yml
  title: ''
  type: Compliance
  url: conformance/reliaquest-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/lifecycle/reliaquest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reliaquest-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/rate-limits/reliaquest-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reliaquest-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/conventions/reliaquest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reliaquest-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/reliaquest/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-18'
description: ReliaQuest is a Tampa-based, privately held cybersecurity company whose GreyMatter platform runs agentic AI security operations (detection, containment, investigation and response) on top of the security tools a customer already owns, connected through bidirectional APIs to 300+ technologies. Customers automate GreyMatter through the GreyMatter API, a single-endpoint GraphQL API (incidents, cases, tasks, detections, playbooks, DRP alerts, discover tasks, users, access groups and API keys) documented as a public Postman collection at apidocs.myreliaquest.com and authenticated with an X-API-KEY header. ReliaQuest also operates the Digital Shadows SearchLight Portal API (digital risk protection) acquired with Digital Shadows in 2022, whose reference is customer-only.
image: https://resources.reliaquest.com/image/upload/c_limit,w_1024,h_1024,f_webp,q_auto/v1725562607/reliaquest-author-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ReliaQuest MCP Server
  slug: reliaquest-mcp-server
modified: '2026-09-18'
name: ReliaQuest
nav: Providers
network: true
overview: 'ReliaQuest publishes 1 API on the [APIs.io](https://apis.io/) network: GreyMatter API. Tagged areas include Cybersecurity, Security Operations, Threat Detection, Incident Response, and Threat Intelligence.


  ReliaQuest''s developer surface includes engineering blog, documentation, API reference, changelog, FAQ, pricing, support, and 24 more developer resources.'
plans:
- name: Reliaquest Plans Pricing
  plan_count: 0
  slug: reliaquest-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Reliaquest Rate Limits
  slug: reliaquest-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Reliaquest Authentication
  slug: reliaquest-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Reliaquest Domain Security
  slug: reliaquest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reliaquest Vulnerability Disclosure
  slug: reliaquest-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Reliaquest Trust Center
  slug: reliaquest-trust-center
  summary_line: SOC 2 Type II, HIPAA, PCI DSS
slug: reliaquest
tags:
- Cybersecurity
- Security Operations
- Threat Detection
- Incident Response
- Threat Intelligence
- Digital Risk Protection
- Agentic AI
- GraphQL
website: https://reliaquest.com/
---
