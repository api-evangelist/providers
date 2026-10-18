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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/codenotary/refs/heads/main/plans/codenotary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codenotary-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codenotary/refs/heads/main/hosts/codenotary-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codenotary-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codenotary/refs/heads/main/vendors/codenotary-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codenotary-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://codenotary.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codenotary.com/terms-of-service?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://support.codenotary.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codenotary.com/privacy-policy?hsLang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://codenotary.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://codenotary.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codenotary
- group: company
  title: ''
  type: Blog
  url: https://codenotary.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codenotary/refs/heads/main/security/codenotary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codenotary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codenotary.com
coverage:
  checked: '2026-10-09'
  detail: The provider's site offers pricing and product information but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://codenotary.com/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Codenotary provides cognitive cybersecurity solutions that monitor, secure, and govern AI agents and autonomous workflows across enterprise environments. Their platform offers real‑time observability, policy enforcement, cost optimization, and compliance for AI‑driven tools, helping organizations prevent rogue AI behavior, data leakage, and security incidents. With products like AgentMon and AgentX, Codenotary enables continuous oversight of millions of agent interactions daily, delivering actionable insights and automated remediation for modern AI‑centric operations.
image: https://codenotary.com/hubfs/Screenshot%202026-09-24%20alle%2010.20.41.png
layout: provider
modified: '2026-10-09'
name: Codenotary
nav: Providers
network: true
overview: 'Codenotary is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cybersecurity, Monitoring, Enterprise, and Platform.


  Codenotary''s developer surface includes support, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Codenotary Plans Pricing
  plan_count: 7
  slug: codenotary-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Codenotary Domain Security
  slug: codenotary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codenotary
tags:
- Artificial Intelligence
- Cybersecurity
- Monitoring
- Enterprise
- Platform
website: https://codenotary.com
---
