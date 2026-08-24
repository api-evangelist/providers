---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 6
asyncapis:
- description: ''
  name: Docstation Webhooks
  slug: docstation-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://docstation.co/
- group: operate
  title: ''
  type: Support
  url: https://help.docstation.co
- group: docs
  title: ''
  type: Documentation
  url: https://help.docstation.co/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.docstation.co/en/collections/2461790-getting-started-with-docstation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocStation
- group: company
  title: ''
  type: Blog
  url: https://docstation.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://docstation.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://docstation.co/get-started
- group: start
  title: ''
  type: Login
  url: https://app.docstation.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docstation.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docstation.co/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docstation.co
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.docstation.co
- group: auth
  title: ''
  type: Compliance
  url: https://docstation.co/platform
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docstation-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docstation-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docstation-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docstation-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/docstation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/docstation-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/docstation-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/docstation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docstation-rate-limits.yml
coverage:
  checked: '2026-08-10'
  detail: DocStation ships only an end-user pharmacy application — there is no api.docstation.co (NXDOMAIN), no developer page in its 217-URL sitemap, and its six named integrations (PioneerRx, Liberty RXQ, DRX, RelayHealth, CPESN, DHS Immunization Gateway) are each enabled from inside the authenticated app with credentials DocStation issues per customer.
  evidence:
  - status: 200
    url: https://docstation.co/sitemap.xml
  - status: 404
    url: https://docstation.co/openapi.json
  - status: 200
    url: https://help.docstation.co/en/articles/4169699-enabling-integrations
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: DocStation is a unified pharmacy care and medical billing platform that helps community and clinical pharmacies move beyond prescription dispensing to bill insurance for the clinical services they already provide — vaccines, MTM, point-of-care testing, consultations, and DME. The platform consolidates 360-degree patient records, automated medical claims generation and resubmission, smart scheduling with public booking links, connected SMS and organization-to-organization messaging, workflow automation, and live revenue analytics into a single system. It integrates with pharmacy management systems (PioneerRx, Liberty, DRX), 1,000+ health plans, clearinghouses, and state immunization registries. DocStation is HIPAA compliant and SOC 2 Type II audited. Backed by Techstars; added to the API Evangelist network and enriched from its public surface. No public developer API is documented at this time.
image: https://docstation.co/api/og?title=Pharmacy+Beyond+Pills.&label=DocStation&accent=blue
layout: provider
modified: '2026-08-10'
name: DocStation
nav: Providers
network: true
overview: 'DocStation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Medical Billing, Healthcare, and Clinical Services.


  The DocStation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DocStation''s developer surface includes support, documentation, getting-started guide, engineering blog, pricing, signup flow, changelog, and 16 more developer resources.'
plans:
- name: Docstation Plans Pricing
  plan_count: 3
  slug: docstation-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Docstation Rate Limits
  slug: docstation-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 52.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docstation/refs/heads/main/screenshots/docstation-2026-07-25T212211.png
security:
- kind: domain-security
  name: Docstation Domain Security
  slug: docstation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docstation Vulnerability Disclosure
  slug: docstation-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Docstation Trust Center
  slug: docstation-trust-center
  summary_line: HIPAA, SOC 2 Type II
slug: docstation
tags:
- Company
- Pharmacy
- Medical Billing
- Healthcare
- Clinical Services
- Patient Management
- Scheduling
- Insurance Claims
- HIPAA
website: https://docstation.co/
---
