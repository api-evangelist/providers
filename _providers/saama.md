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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.saama.com/about/company/security-compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saamaresearch
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saama-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/saama-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/saama-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/saama-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/saama-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/saama-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saama.com/
- group: company
  title: ''
  type: Blog
  url: https://www.saama.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.saama.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://www.saama.com/news/
- group: operate
  title: ''
  type: Support
  url: https://support.saama.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saama.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saama.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saama-technologies
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/saama_stock/
coverage:
  checked: '2026-08-26'
  detail: Saama serves no developer host at all - developer.saama.com, docs.saama.com, api.saama.com, apidocs.saama.com, mcp.saama.com and status.saama.com are every one of them DNS NXDOMAIN - and on the marketing site /api/, /developers/ and /docs/ all HTTP 301 straight back to the homepage, so the API its own Smart Medical Coding page advertises ("inbound/outbound APIs, EDC connectors, and token-based authentication") is documented only behind support.saama.com, which 302s to a Freshdesk customer login.
  evidence:
  - status: 301
    url: https://www.saama.com/api/
  - status: 301
    url: https://www.saama.com/developers/
  - status: 301
    url: https://www.saama.com/docs/
  - status: <no response>
    url: https://developer.saama.com/
  - status: <no response>
    url: https://api.saama.com/
  - status: 302
    url: https://support.saama.com/
  - status: 404
    url: https://www.saama.com/llms.txt
  - status: 404
    url: https://www.saama.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Saama (Saama Technologies, Inc.) is a Campbell, California life-sciences technology company that builds AI-powered clinical analytics software for biopharmaceutical sponsors and CROs. Its platform ingests, curates and animates clinical trial data through products including the Data Hub, Smart Data Quality (SDQ), Operational Insights, Patient Insights, Source to Submission (S2S) and the BRAIN family (BRAIN SDTM, BRAIN SCE, BRAIN Visualization, BRAIN Consortium), alongside a set of modular Clinical AI Agents announced in 2025. Saama states its platform offers 40-plus pre-built connectors and that its agents are "connected via APIs", but as of this profile the company publishes no public developer portal, API reference or machine-readable specification - technical documentation and the support portal both sit behind a customer login.
image: https://www.saama.com/wp-content/uploads/hero.png
layout: provider
modified: '2026-08-26'
name: Saama
nav: Providers
network: true
overview: 'Saama is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Life Sciences, Clinical Trials, Clinical Data Management, Analytics, and Artificial Intelligence.


  Saama''s developer surface includes engineering blog, support, and 16 more developer resources.'
plans:
- name: Saama Plans Pricing
  plan_count: 0
  slug: saama-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Saama Rate Limits
  slug: saama-rate-limits
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Saama Authentication
  slug: saama-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Saama Domain Security
  slug: saama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Saama Trust Center
  slug: saama-trust-center
  summary_line: ISO/IEC 27001:2013, 21 CFR Part 11, ICH E6 (Good Clinical Practice), FIPS 140-2
slug: saama
tags:
- Life Sciences
- Clinical Trials
- Clinical Data Management
- Analytics
- Artificial Intelligence
- Machine-Learning
- Pharmaceuticals
- Healthcare
- Data Platform
- CDISC
website: https://www.saama.com/
---
