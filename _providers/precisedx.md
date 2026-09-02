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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/precisedx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.precisedx.ai/
- group: start
  title: ''
  type: Login
  url: https://portal.precisedx.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.precisedx.ai/portal-signup
- group: operate
  title: ''
  type: Support
  url: https://www.precisedx.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.precisedx.ai/publications
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PreciseDx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.precisedx.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.precisedx.ai/terms-of-service
- group: auth
  title: ''
  type: Compliance
  url: https://www.precisedx.ai/certifications
- group: design
  title: ''
  type: Conformance
  url: conformance/precisedx-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/precisedx-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PreciseDx is a CLIA-certified clinical laboratory whose product is an ordered breast cancer prognostic test, not software — clinicians order PreciseBreast through an email-and-password web portal at portal.precisedx.ai and no api., docs. or developer. subdomain resolves in DNS at all.
  evidence:
  - status: 200
    url: https://portal.precisedx.ai/
  - status: 404
    url: https://portal.precisedx.ai/openapi.json
  - status: 404
    url: https://www.precisedx.ai/openapi.json
  - status: 404
    url: https://www.precisedx.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.precisedx.ai/llms.txt
  - status: 200
    url: https://api.github.com/orgs/PreciseDx/repos
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: PreciseDx is a New York-based AI digital pathology and oncology diagnostics company, founded out of the digital pathology program at Mount Sinai Health System. Its OncoIntelligence platform applies a patented Morphology Feature Array to hematoxylin and eosin (H&E) stained tissue images, combining AI-derived morphology features with clinicopathologic factors to produce an OncoIntelligence Score. The flagship test, PreciseBreast, stratifies early-stage breast cancer patients into high- and low-risk cohorts for disease recurrence up to 8.8 years, clinically validated across more than 1,600 cases, returning results in hours rather than the two to six weeks required for gene expression testing and at roughly 30 percent of the cost. PreciseDx operates CLIA-certified and CAP-accredited laboratories in New York City and Miami and is licensed in all 50 states. Test ordering for clinicians is handled through an authenticated web portal; the company publishes no public developer program,
  API documentation, or machine-readable API contract.
image: https://cdn.prod.website-files.com/67378b4f7c5e7a479024673e/6744ba2778d8a8afb2c924d1_PreciseDx-Webclip.svg
layout: provider
modified: '2026-08-26'
name: PreciseDx
nav: Providers
network: true
overview: 'PreciseDx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Digital Pathology.


  PreciseDx''s developer surface includes signup flow, support, engineering blog, and 9 more developer resources.'
plans:
- name: Precisedx Plans Pricing
  plan_count: 0
  slug: precisedx-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Precisedx Rate Limits
  slug: precisedx-rate-limits
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.1
  provenance:
    conformance: first-party
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
- kind: domain-security
  name: Precisedx Domain Security
  slug: precisedx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: precisedx
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Digital Pathology
- Oncology
- Artificial Intelligence
- Machine-Learning
- Clinical Laboratory
- Precision Medicine
website: https://www.precisedx.ai/
---
