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
api_count: 1
apis:
- description: Cofactor AI does not publish a public developer program or API documentation.
  name: Cofactor AI API
  slug: cofactor-ai-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.cofactorai.com/security-compliance
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cofactor-ai/refs/heads/main/hosts/cofactor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cofactor-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cofactor-ai/refs/heads/main/vendors/cofactor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cofactor-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cofactorai
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cofactor-ai/refs/heads/main/security/cofactor-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cofactor-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cofactor-ai/refs/heads/main/security/cofactor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofactor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cofactorai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cofactorai.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cofactorai.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cofactorai.com/legal/terms-of-service
coverage:
  checked: '2026-10-09'
  detail: Documentation page https://www.cofactorai.com/docs returns 404, indicating no public API docs.
  evidence:
  - status: 404
    url: https://www.cofactorai.com/docs
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cofactor AI provides AI‑driven solutions for healthcare providers, enabling smarter clinical workflows, predictive analytics, and automated documentation. Their platform integrates with electronic health record systems to improve patient outcomes and operational efficiency across hospitals and clinics.
layout: provider
modified: '2026-10-09'
name: Cofactor AI
nav: Providers
network: true
overview: 'Cofactor AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Platform, and Analytics.


  Cofactor AI''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cofactor Ai Domain Security
  slug: cofactor-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cofactor Ai Trust Center
  slug: cofactor-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: cofactor-ai
tags:
- Company
- Healthcare
- Artificial Intelligence
- Platform
- Analytics
website: https://www.cofactorai.com/
---
