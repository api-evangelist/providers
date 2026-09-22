---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Teamleader Webhooks
  slug: teamleader-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/well-known/teamleader-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teamleader-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/well-known/teamleader-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teamleader-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamleader.eu/legal/terms-of-service-teamleader-focus
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/asyncapi/teamleader-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/teamleader-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/changelog/teamleader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/teamleader-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.teamleader.eu/legal/security-teamleader-focus
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/teamleader-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/llms/teamleader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teamleader-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/packages/teamleader-packages.yml
  title: ''
  type: SDKs
  url: packages/teamleader-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/packages/teamleader-packages.yml
  title: ''
  type: Packages
  url: packages/teamleader-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teamleader.eu/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/teamleader-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teamleader-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teamleader/refs/heads/main/security/teamleader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teamleader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamleader.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.focus.teamleader.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.focus.teamleader.eu/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.focus.teamleader.eu/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.focus.teamleader.eu/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.focus.teamleader.eu/hc/en-150
- group: company
  title: ''
  type: Blog
  url: https://www.teamleader.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamleader.eu/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamleader.eu/legal/privacy-statement
- group: start
  title: ''
  type: SignUp
  url: https://signup.focus.teamleader.eu/
coverage:
  checked: 2026-09-21
  detail: Developer docs provide markdown but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://api.teamleader.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Teamleader provides an integrated CRM, invoicing, quotations, and project management platform for SMEs. Its Focus product offers a unified workspace to manage customers, sales, finances, and projects, with a marketplace for extensions and robust API access for developers.
image: https://cdn.craft.cloud/019c94d2-1a0c-72a9-9aeb-fca40a9cddd3/assets/general/SEO-images/Teamleader-SEO.jpg?fit=cover&height=630&width=1200&s=qRou8Ix0kelrG98e5NrDsPf-6SZBB_wNOxzMj9zJnug
layout: provider
modified: '2026-09-21'
name: Teamleader
nav: Providers
network: true
overview: 'Teamleader is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Invoicing, Project Management, Software-as-a-Service, and SME.


  The Teamleader catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teamleader''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 57.4
    operational_transparency: 50.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Teamleader Domain Security
  slug: teamleader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Teamleader Vulnerability Disclosure
  slug: teamleader-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Teamleader Trust Center
  slug: teamleader-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: teamleader
tags:
- CRM
- Invoicing
- Project Management
- Software-as-a-Service
- SME
website: https://www.teamleader.eu/
---
