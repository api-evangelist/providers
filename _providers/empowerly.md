---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: https://status.empowerly.com/api/v2
  baseurl_source: declared
  description: Read-only, unauthenticated JSON status API served from Empowerly's own status subdomain by Atlassian Statuspage. Exposes the overall page status indicator, the component roster (currently a single "Em
  name: Empowerly Status API
  slug: empowerly-status-api
- baseURL: https://status.empowerly.com/api/v2
  baseurl_source: declared
  description: The individual platform components Empowerly reports on.
  name: Empowerly Components API
  slug: empowerly-components-api
- baseURL: https://status.empowerly.com/api/v2
  baseurl_source: declared
  description: Incident history and currently unresolved incidents.
  name: Empowerly Incidents API
  slug: empowerly-incidents-api
- baseURL: https://status.empowerly.com/api/v2
  baseurl_source: declared
  description: Scheduled maintenance windows.
  name: Empowerly Maintenance API
  slug: empowerly-maintenance-api
artifact_total: 11
collections:
- collection_type: open
  name: Empowerly Status API
  slug: open-empowerly-status-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/empowerly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/empowerly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/empowerly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://empowerly.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/empowerly_stock/
- group: company
  title: ''
  type: Blog
  url: https://empowerly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://empowerly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://empowerly.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://empowerly.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.empowerly.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/empowerly
- group: operate
  title: ''
  type: StatusPage
  url: https://status.empowerly.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/empowerly-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/empowerly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/empowerly-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/empowerly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/empowerly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/empowerly-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/empowerly-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/empowerly-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/empowerly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/empowerly-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/empowerly-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/empowerly-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/empowerly-well-known.yml
coverage:
  checked: '2026-08-12'
  detail: Empowerly runs a live production API host (api.empowerly.com/health returns 200 "Empowerly Production API is up and running") purely as the private backend for its student web portal, and publishes nothing around it — no developer portal, no docs, no spec, no SDKs, no GitHub org; developer.empowerly.com and docs.empowerly.com do not even resolve.
  evidence:
  - status: 200
    url: https://api.empowerly.com/health
  - status: 404
    url: https://api.empowerly.com/openapi.json
  - status: 404
    url: https://empowerly.com/developers
  - status: 404
    url: https://empowerly.com/api
  - status: 403
    url: https://empowerly.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/empowerly
  - status: 200
    url: https://status.empowerly.com/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Empowerly is an education-technology company founded in 2017 by Hanmei Wu and Changxiao Xie that delivers personalized college admissions and career counseling to high-school students. The platform pairs students with a network of more than 100 counselors — including former college admission officers — and layers on data-driven tooling: a proprietary admissions calculator built from thousands of past student outcomes, college-list building, essay editing and review, interview preparation, and startup and research internship placement programs. Students and families work through the Empowerly web portal at app.empowerly.com; counseling packages are sold through an enrollment conversation rather than published price tiers. Empowerly publishes no public developer program, API documentation, or SDKs; the only publicly callable surface on its own domains is the Atlassian-hosted status page API at status.empowerly.com.'
image: https://empowerly.com/empowerly-icon.png
layout: provider
modified: '2026-08-12'
name: Empowerly
nav: Providers
network: true
overview: 'Empowerly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Status API, Components API, Incidents API, and 1 more. Tagged areas include Company, Education, EdTech, College Admissions, and Counseling.


  Empowerly''s developer surface includes engineering blog, pricing, authentication, and 23 more developer resources.'
plans:
- name: Empowerly Plans Pricing
  plan_count: 0
  slug: empowerly-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Empowerly Rate Limits
  slug: empowerly-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 12.7
    developer_ergonomics: 25.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 37.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/empowerly/refs/heads/main/screenshots/empowerly-2026-09-02T145352.png
security:
- kind: authentication
  name: Empowerly Authentication
  slug: empowerly-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Empowerly Domain Security
  slug: empowerly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Empowerly Vulnerability Disclosure
  slug: empowerly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Empowerly Trust Center
  slug: empowerly-trust-center
  summary_line: SOC 2 Type 2
slug: empowerly
tags:
- Company
- Education
- EdTech
- College Admissions
- Counseling
- Students
- Career Services
- Consumer Services
- Status Page
website: https://empowerly.com/
---
