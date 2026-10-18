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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognni/refs/heads/main/hosts/cognni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognni-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognni/refs/heads/main/vendors/cognni-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognni-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognni
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognni/refs/heads/main/security/cognni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognni.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cognni.com/what-we-do
- group: company
  title: ''
  type: Blog
  url: https://www.cognni.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cognni.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognni.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.cognni.com/contact-us
coverage:
  checked: '2026-10-09'
  detail: Cognni's website provides product information but no developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.cognni.com/what-we-do
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cognni provides a Knowledge Management Software and Insights Platform that centralizes, organizes, and makes actionable the vast amounts of knowledge within an organization. Leveraging generative AI, Cognni transforms raw data, research, and insights into usable information, enabling faster, data‑driven decisions. The platform offers features such as knowledge centralization, AI‑powered search, collaboration tools, and integration with existing data sources, helping enterprises break down silos and unlock the value of their collective intelligence.
image: http://static1.squarespace.com/static/65378c6c20872b1c0fdd9de3/t/65b398cbe1f0d036eb22a21b/1706268879319/Cognni+Sparkle+Woman+B+Corp+Image+1.PNG?format=1500w
layout: provider
modified: '2026-10-09'
name: Cognni
nav: Providers
network: true
overview: 'Cognni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Knowledge Management, Generative AI, Enterprise Software, Collaboration, and Insights.


  Cognni''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognni Domain Security
  slug: cognni-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cognni
tags:
- Knowledge Management
- Generative AI
- Enterprise Software
- Collaboration
- Insights
website: https://www.cognni.com
---
