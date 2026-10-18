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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.optro.ai/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/conformance/auditboard-reenrich-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auditboard-reenrich-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/llms/auditboard-reenrich-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auditboard-reenrich-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/hosts/auditboard-reenrich-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auditboard-reenrich-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/vendors/auditboard-reenrich-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auditboard-reenrich-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optro.ai/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://optro.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://optro.ai/news
- group: company
  title: ''
  type: Blog
  url: https://optro.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://optro.ai/exchange/best-practice-guide-getting-started-with-an-ai-first-approach-to-audit-in-auditboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/security/auditboard-reenrich-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/auditboard-reenrich-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auditboard-reenrich/refs/heads/main/security/auditboard-reenrich-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auditboard-reenrich-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optro.ai
coverage:
  checked: '2026-10-13'
  detail: The provider's website https://optro.ai offers documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://optro.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: AuditBoard, now operating as Optro, provides AI‑powered governance, risk, and compliance (GRC) software for enterprises. Its platform combines real‑time risk intelligence, autonomous testing, and integrated audit tools to help organizations streamline risk management, compliance, and internal audit processes. With a focus on modern cloud‑based solutions, Optro serves over half of the Fortune 500, offering modules for audit, risk, IT compliance, and continuous monitoring, all powered by AI and analytics.
image: https://cdn.sanity.io/images/rmkwjgaf/production-churro/4dc2ef110eb5013e1f3a6ba590de3fdc26471fe1-1200x630.jpg?w=1200&fit=max&auto=format
layout: provider
modified: '2026-10-12'
name: AuditBoard
nav: Providers
network: true
overview: 'AuditBoard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GRC, Artificial Intelligence, Enterprise, and Compliance.


  AuditBoard''s developer surface includes pricing, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auditboard Reenrich Domain Security
  slug: auditboard-reenrich-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Auditboard Reenrich Trust Center
  slug: auditboard-reenrich-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR, CSA STAR
slug: auditboard-reenrich
tags:
- Company
- GRC
- Artificial Intelligence
- Enterprise
- Compliance
website: https://optro.ai
---
