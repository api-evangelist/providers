---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Cloudidr Agentic Access
  operation_count: 12
  slug: cloudidr-agentic-access
  summary_line: 12 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://public-api.cloudidr.com
  baseurl_source: declared
  description: The External API from Cloudidr — 12 operation(s) for external.
  name: Cloudidr External API
  slug: cloudidr-external-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/agentic-access/cloudidr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudidr-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/plans/cloudidr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudidr-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/rules/cloudidr-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudidr-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/authentication/cloudidr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudidr-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/errors/cloudidr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudidr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/conformance/cloudidr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudidr-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/overlays/cloudidr-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/cloudidr-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/llms/cloudidr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudidr-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/a2a/cloudidr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cloudidr-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/well-known/cloudidr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudidr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/hosts/cloudidr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudidr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/vendors/cloudidr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudidr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudidr.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudidr.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudidr.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.cloudidr.com/blog
- group: start
  title: ''
  type: SignUp
  url: http://llm-ops.cloudidr.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudidr.com/guides/llm-ops/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudidr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloudidr.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudidr/refs/heads/main/security/cloudidr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudidr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudidr.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.cloudidr.com/mcp
  - status: 200
    url: https://cloudidr.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Cloudidr provides a cloud-based identity and access management platform that enables enterprises to securely manage user authentication, authorization, and lifecycle across multiple applications and services. The solution offers features such as single sign‑on (SSO), multi‑factor authentication (MFA), role‑based access control, and automated provisioning. Designed for scalability and compliance, Cloudidr helps organizations meet security standards while simplifying user management and improving operational efficiency.
image: https://framerusercontent.com/assets/F2tSiREZaPKoP6x8PGivmwaUFs4.png
layout: provider
modified: '2026-10-16'
name: Cloudidr
nav: Providers
network: true
overview: 'Cloudidr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Identity and Access Management, Cloud, Security, and Artificial Intelligence.


  The Cloudidr catalog on APIs.io includes 1 Spectral governance ruleset.


  Cloudidr''s developer surface includes authentication, pricing, engineering blog, signup flow, getting-started guide, documentation, API reference, and 15 more developer resources.'
plans:
- name: Cloudidr Plans Pricing
  plan_count: 4
  slug: cloudidr-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cloudidr API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 4
  slug: cloudidr-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.2
    developer_ergonomics: 42.9
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudidr Authentication
  slug: cloudidr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cloudidr Domain Security
  slug: cloudidr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudidr
tags:
- Company
- Identity and Access Management
- Cloud
- Security
- Artificial Intelligence
- FinOps
website: https://cloudidr.com/
---
