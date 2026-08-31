---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: Browser-side JavaScript API for the Osano Consent Management Platform, loaded from cmp.osano.com. Exposes functions (showDialog, showDrawer, getConsent, ready, addEventListener), properties (consentMo
  name: Osano CMP JavaScript API
  slug: osano-cmp-javascript-api
- description: The cmp API from Osano — 6 operation(s) for cmp.
  name: Osano Cmp API
  slug: osano-cmp-api
- description: The cmpRules API from Osano — 2 operation(s) for cmprules.
  name: Osano Cmp Rules API
  slug: osano-cmprules-api
- description: The Collections API from Osano — 2 operation(s) for collections.
  name: Osano Collections API
  slug: osano-collections-api
- description: The Config API from Osano — 1 operation(s) for config.
  name: Osano Config API
  slug: osano-config-api
- description: The connectors API from Osano — 1 operation(s) for connectors.
  name: Osano Connectors API
  slug: osano-connectors-api
- description: The Consent Profiles API from Osano — 1 operation(s) for consent profiles.
  name: Osano Consent Profiles API
  slug: osano-consent-profiles-api
- description: The Consents API from Osano — 4 operation(s) for consents.
  name: Osano Consents API
  slug: osano-consents-api
- description: The customerInsights API from Osano — 1 operation(s) for customerinsights.
  name: Osano Customer Insights API
  slug: osano-customerinsights-api
- description: Discover and manage data stores and personal data fields
  name: Osano Data Discovery API
  slug: osano-datadiscovery-api
- description: Manage subject rights requests and data subject access requests
  name: Osano Dsar API
  slug: osano-dsar-api
- description: Manage action items for subject rights requests
  name: Osano Dsar Action Items API
  slug: osano-dsaractionitems-api
- description: The Sessions API from Osano — 1 operation(s) for sessions.
  name: Osano Sessions API
  slug: osano-sessions-api
- description: The subjectRightsPortal API from Osano — 2 operation(s) for subjectrightsportal.
  name: Osano Subject Rights Portal API
  slug: osano-subjectrightsportal-api
- description: The Subjects API from Osano — 9 operation(s) for subjects.
  name: Osano Subjects API
  slug: osano-subjects-api
- description: The Token API from Osano — 1 operation(s) for token.
  name: Osano Token API
  slug: osano-token-api
- description: The Unified Consent Core API API from Osano — 1 operation(s) for unified consent core api.
  name: Osano Unified Consent Core API
  slug: osano-unified-consent-core-api-api
artifact_total: 24
asyncapis:
- description: ''
  name: Osano Webhooks
  slug: osano-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/osano-customer-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/osano-unified-consent-core-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.osano.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.osano.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.osano.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.osano.com/customer-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.osano.com/customer-rest-api/developer-api-doc
- group: operate
  title: ''
  type: Support
  url: https://docs.osano.com/en-US/osano/directories
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.osano.com/en-US/osano/directories
- group: company
  title: ''
  type: Blog
  url: https://www.osano.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/osano
- group: commercial
  title: ''
  type: Pricing
  url: https://www.osano.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://my.osano.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osano.trusthub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osano.trusthub.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.osano.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.osano.com/
- group: build
  title: ''
  type: Packages
  url: packages/osano-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/osano-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/osano-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osano-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/osano-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/osano-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osano-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osano-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/osano-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osano-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osano-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/osano-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/osano-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osano-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/osano-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/osano-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/osano-rate-limits.yml
- group: operate
  title: ''
  type: SLA
  url: https://osano.trusthub.com/sls
- group: other
  title: ''
  type: Subprocessors
  url: https://osano.trusthub.com/subprocessors
created: '2026-08-26'
description: Osano is a data privacy platform, founded in 2018 and headquartered in Austin, Texas, that helps organizations build and run privacy programs across consent management, subject rights (DSAR) automation, data mapping and discovery, privacy assessments, and vendor privacy risk management. It is a certified B Corporation and Public Benefit Corporation, and backs the platform with a "No Fines. No Penalties." guarantee covering GDPR, CPRA/CCPA and 95+ global privacy laws. Developers reach the platform through two public REST APIs — the Osano Customer REST API (api.osano.com) for cookie consent configurations, rules, audit logs, subject rights requests, action items and data discovery, and the Unified Consent Core API (uc.api.osano.com) for collecting, checking and merging consent for subjects across cookie and non-cookie touchpoints — plus a browser CMP JavaScript API, iOS/Android/React Native SDKs, a Unified Consent JS SDK, and outbound webhooks. Osano also operates OsanoBot, a
  compliance scanning crawler that authenticates itself with Web Bot Auth (RFC 9421 HTTP Message Signatures) and publishes its Ed25519 key directory publicly.
image: https://avatars.githubusercontent.com/u/40547146?v=4
layout: provider
modified: '2026-08-26'
name: Osano
nav: Providers
network: true
overview: 'Osano publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Cmp API, Cmp Rules API, Collections API, and 13 more. Tagged areas include Company, Data Privacy, Consent Management, Compliance, and GDPR.


  The Osano catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Osano''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Osano Plans Pricing
  plan_count: 3
  slug: osano-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Osano Rate Limits
  slug: osano-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 4.5
    contract_quality: 57.7
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 54.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Osano Authentication
  slug: osano-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Osano Domain Security
  slug: osano-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Osano Vulnerability Disclosure
  slug: osano-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Osano Trust Center
  slug: osano-trust-center
  summary_line: SOC 2, Enterprise audit package
slug: osano
tags:
- Company
- Data Privacy
- Consent Management
- Compliance
- GDPR
- CCPA
- Cookie Consent
- Subject Rights
- Data Mapping
- Vendor Risk
- Privacy Assessments
- Governance Risk Compliance
website: https://www.osano.com/
---
