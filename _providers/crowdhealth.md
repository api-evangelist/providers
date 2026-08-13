---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joincrowdhealth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joincrowdhealth.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.joincrowdhealth.com/registration/new
- group: start
  title: ''
  type: Login
  url: https://app.joincrowdhealth.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joincrowdhealth.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joincrowdhealth.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.joincrowdhealth.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.joincrowdhealth.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.joincrowdhealth.com/resources/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JoinCrowdHealth
- group: auth
  title: ''
  type: Security
  url: https://www.joincrowdhealth.com/data-security
- group: auth
  title: ''
  type: Compliance
  url: https://www.joincrowdhealth.com/data-security
- group: commercial
  title: ''
  type: Plans
  url: plans/crowdhealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crowdhealth-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crowdhealth-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdhealth-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crowdhealth-llms.txt
coverage:
  checked: '2026-08-12'
  detail: CrowdHealth is a consumer health-crowdfunding app with no developer program at all — its only API is a private Apollo GraphQL endpoint at api.joincrowdhealth.com/graphql that backs its own web and mobile apps, and that endpoint answers introspection with INTROSPECTION_DISABLED, so no contract exists to read even for its own clients.
  evidence:
  - status: 400
    url: https://api.joincrowdhealth.com/graphql
  - status: 404
    url: https://api.joincrowdhealth.com/openapi.json
  - status: 404
    url: https://www.joincrowdhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.joincrowdhealth.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'CrowdHealth is an Austin, Texas company offering community-powered health care crowdfunding as an alternative to traditional health insurance. Members pay a monthly membership (advocacy) fee and commit a monthly contribution amount that is used to fund other members'' eligible medical bills peer-to-peer, without premiums, networks, or claim denials. The platform bundles bill negotiation, personal care advocates, provider search, prescription discounts and care navigation into a consumer web app and iOS/Android mobile apps. CrowdHealth is a consumer product company: it operates a private Apollo GraphQL backend at api.joincrowdhealth.com that serves its own apps, but publishes no public API, SDK, developer portal, or machine-readable contract of any kind.'
image: https://cdn.prod.website-files.com/60db2ced4a27795173580197/65bba6a83a452a08f68cd220_Open%20Graph%20Image%20V2.png
layout: provider
modified: '2026-08-12'
name: CrowdHealth
nav: Providers
network: true
overview: 'CrowdHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Health Care, Health Insurance, and Health Sharing.


  CrowdHealth''s developer surface includes pricing, signup flow, engineering blog, support, FAQ, and 13 more developer resources.'
plans:
- name: Crowdhealth Plans Pricing
  plan_count: 1
  slug: crowdhealth-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 0
  name: Crowdhealth Rate Limits
  slug: crowdhealth-rate-limits
score:
  band: thin
  composite: 28.4
  facets:
    commercial_clarity: 73.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Crowdhealth Domain Security
  slug: crowdhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crowdhealth Vulnerability Disclosure
  slug: crowdhealth-vulnerability-disclosure
  summary_line: Hackerone
slug: crowdhealth
tags:
- Company
- Health
- Health Care
- Health Insurance
- Health Sharing
- Crowdfunding
- Medical Billing
- Consumer Health
- Insurance Alternative
- Fintech
website: https://www.joincrowdhealth.com/
---
