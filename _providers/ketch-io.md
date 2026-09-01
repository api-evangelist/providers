---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ketch Io Agentic Access
  operation_count: 6
  slug: ketch-io-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: REST API for the Ketch platform that powers consent collection and enforcement, data subject rights workflows, data mapping, preference management, and risk reporting. Endpoints are served from global
  name: Ketch API
  slug: ketch-api
- description: TypeScript and JavaScript Web API and consent library for collecting, storing, and enforcing consent in browser environments. Includes methods such as getBootstrapConfiguration and getConsent and a co
  name: Ketch Web SDK
  slug: ketch-web-sdk
- description: Native iOS and Android SDKs for collecting and enforcing consent in mobile apps. The iOS SDK supports iOS 15 and above; the Android SDK targets API level 26 and above. Supports preemptive consent coll
  name: Ketch Mobile SDKs
  slug: ketch-mobile-sdks
- description: Fetch per-property bootstrap and consent configuration.
  name: Ketch Configuration API
  slug: ketch-io-configuration-api
- description: Retrieve and update visitor consent state.
  name: Ketch Consent API
  slug: ketch-io-consent-api
- description: Generate QR codes for the preference center.
  name: Ketch Preferences API
  slug: ketch-io-preferences-api
- description: Submit data subject right requests (access, deletion, etc).
  name: Ketch Rights API
  slug: ketch-io-rights-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ketch Web Configuration API
  slug: open-ketch-io-configuration-api
- collection_type: open
  name: Ketch Web Configuration Consent API
  slug: open-ketch-io-consent-api
- collection_type: open
  name: Ketch Web Configuration Preferences API
  slug: open-ketch-io-preferences-api
- collection_type: open
  name: Ketch Web Configuration Rights API
  slug: open-ketch-io-rights-api
- collection_type: open
  name: Ketch Web API
  slug: open-ketch-io
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ketch-sdk/ketch-web-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ketch-sdk/ketch-web-api/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ketch-sdk/ketch-web-api/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ketch-sdk/ketch-web-api/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ketch-sdk/ketch-web-api/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ketch-sdk/ketch-web-api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ketch-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ketch-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ketch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ketch.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ketch-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ketch-com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ketch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ketch.com/blog
created: '2026-05-23'
description: Ketch is a data permissioning and consent platform that helps enterprises keep customer data clean, permissioned, and AI-ready across web, mobile, and backend systems. Its products span consent management, data subject rights automation, AI-powered data mapping, marketing preference management, risk and reporting, a Data Sentry privacy pentest, and an AI governance layer. The Ketch Agent Network turns privacy program insights into agent-driven actions. Builders use a public REST API hosted at global.ketchapi.com, web and mobile SDKs published on GitHub, and Google Tag Manager templates to enforce consent at the source. Ketch advertises more than 1,000 pre-built API integrations with systems, apps, and AI models, with a free tier alongside enterprise and mid-market editions.
finops:
- name: Ketch Io Finops
  service_category: API
  slug: ketch-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ketch-io.png
layout: provider
modified: '2026-05-23'
name: Ketch
nav: Providers
network: true
overview: 'Ketch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Consent API, Preferences API, and 1 more. Tagged areas include Ketch, Privacy, Consent, Preference Management, and DSR.


  Ketch''s developer surface includes documentation, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Ketch Io Plans Pricing
  plan_count: 1
  slug: ketch-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Ketch Io Rate Limits
  slug: ketch-io-rate-limits
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 46.6
    developer_ergonomics: 10.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ketch-io/refs/heads/main/screenshots/ketch-io-2026-06-20T183959.png
security:
- kind: domain-security
  name: Ketch Io Domain Security
  slug: ketch-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ketch-io
tags:
- Ketch
- Privacy
- Consent
- Preference Management
- DSR
- Data Mapping
- AI Governance
- GDPR
- CCPA
- SDK
- Mobile
- Web
website: https://www.ketch.com/
---
