---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Authenticated REST administration and reporting surface for the iboss Zero Trust SASE/SSE cloud platform, served under the /ibcloud/web path on the iboss cloud gateway hosts. Probed anonymously it ans
  name: iboss Zero Trust SSE Platform API
  slug: iboss-zero-trust-sse-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iboss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iboss.com
- group: operate
  title: ''
  type: Support
  url: https://www.iboss.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ibosscloud.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.iboss.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.iboss.com/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iboss.com/pricing
- group: start
  title: ''
  type: Login
  url: https://accounts.iboss.com/ibossauth/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iboss.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iboss.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iboss.com/ibcloud/app/cloudStatus.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.iboss.com/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iboss-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iboss-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iboss-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iboss-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iboss-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iboss-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iboss-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iboss-plans-pricing.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/iboss-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/iboss-packages.yml
coverage:
  checked: '2026-08-22'
  detail: 'iboss runs a live platform API — api.ibosscloud.com/ibcloud/web answers HTTP 401 with XSRF-TOKEN and JSESSIONID cookies and a "Server: iboss cloud" header — but publishes no contract for it: docs.iboss.com 307-redirects to a sign-in-gated app.gitbook.com space rather than a published docs site, and the 344-URL sitemap contains no /api, /developer or /reference route.'
  evidence:
  - status: 401
    url: https://api.ibosscloud.com/ibcloud/web/users
  - status: 307
    url: https://docs.iboss.com
  - status: 404
    url: https://api.ibosscloud.com/openapi.json
  - status: 200
    url: https://www.iboss.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-22'
description: iboss, Inc. is a Boston-headquartered cybersecurity company founded in 2003 that operates an AI-powered, cloud-native Zero Trust SASE (Secure Access Service Edge) platform used by more than 4,000 enterprise, US federal, state and local government, and K-12 education organizations. The platform consolidates Secure Web Gateway (SWG), Cloud Access Security Broker (CASB), Zero Trust Network Access (ZTNA), Data Loss Prevention (DLP), Remote Browser Isolation (RBI), SaaS Security Posture Management (SSPM), DNS security, SD-WAN and AI chat monitoring into a single containerized service in which each customer receives dedicated gateway containers rather than shared infrastructure. iboss is FedRAMP and StateRAMP authorized and holds SOC 2 Type II, FIPS 140-2, HIPAA, CJIS, FERPA and GDPR alignment. Platform administration and reporting run over an authenticated REST surface at api.ibosscloud.com/ibcloud/web, which third parties including Datadog, Axonius, Google Security Operations and
  D3 Security integrate against; iboss publishes no public OpenAPI definition, developer portal or API reference, and its documentation host redirects to a sign-in-gated GitBook space.
image: https://www.iboss.com/favicon.ico
layout: provider
modified: '2026-08-22'
name: iboss
nav: Providers
network: true
overview: 'iboss publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Zero Trust, and SASE.


  iboss'' developer surface includes support, engineering blog, pricing, authentication, and 18 more developer resources.'
plans:
- name: Iboss Plans Pricing
  plan_count: 3
  slug: iboss-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Iboss Rate Limits
  slug: iboss-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 23.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Iboss Authentication
  slug: iboss-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Iboss Domain Security
  slug: iboss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Iboss Trust Center
  slug: iboss-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO 27001, ISO 9001, FedRAMP Authorized, StateRAMP Authorized, CJIS, CSA STAR Level 1, CSA STAR Level 2, Cyber Essentials, CMMC 2.0, FIPS 140-2, HIPAA, FERPA, GDPR
slug: iboss
tags:
- Company
- Security
- Cybersecurity
- Zero Trust
- SASE
- Secure Web Gateway
- CASB
- ZTNA
- Data Loss Prevention
- Network Security
- Cloud Security
- Compliance
website: https://www.iboss.com
---
