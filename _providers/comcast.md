---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - '{''url'': ''https://www.comcast.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.xfinity.com/ — a different registrable domain (comcast.com -> xfinity.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Firebolt is Comcast's application platform for building apps that run on TVs, set-top boxes, and other connected home devices. The Firebolt SDK exposes a family of JavaScript APIs (Lifecycle, Metrics,
  name: Comcast Firebolt SDK
  slug: firebolt-sdk
- description: The Comcast Security Access Token (SAT) endpoint issues short-lived bearer tokens used to authenticate calls to Comcast partner APIs such as the Open Ingest service. Clients exchange an x-client-id an
  name: Comcast Authentication API (SAT)
  slug: authentication-api
- description: The Comcast Open Ingest endpoint accepts metadata and content asset packages from NBCUniversal media partners. Clients POST an XML payload describing assets to the Merlin ingest proxy, authenticated w
  name: Comcast Open Ingest API
  slug: open-ingest-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comcast-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comcast
- group: company
  title: ''
  type: Website
  url: https://www.comcast.com
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.developer.comcast.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.comcast.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Comcast
- group: other
  title: ''
  type: OpenSource
  url: https://comcast.github.io/
- group: other
  title: ''
  type: Xfinity
  url: https://www.xfinity.com/
- group: other
  title: ''
  type: NBCUniversal
  url: https://www.nbcuniversal.com/
- group: company
  title: ''
  type: Investors
  url: https://www.cmcsa.com/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.xfinity.com/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.xfinity.com/TOS.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/comcast-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.developer.comcast.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.comcast.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.comcast.com/docs/firebolt-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.comcast.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.developer.comcast.com/docs/getting-help
- group: start
  title: ''
  type: SignUp
  url: https://developer.comcast.com/portal/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rdkcentral
- group: agent
  title: ''
  type: WellKnown
  url: well-known/comcast-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/comcast-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/comcast-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/comcast-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/comcast-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/comcast-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/comcast-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/comcast-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/comcast-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/comcast-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/comcast-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/comcast-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/comcast-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/comcast-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/comcast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/comcast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/comcast-finops.yml
- group: auth
  title: ''
  type: Security
  url: security/comcast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/comcast-vulnerability-disclosure.yml
created: '2026-03-21'
description: Comcast Corporation is a global media and technology company with two primary businesses, Comcast Cable (Xfinity) and NBCUniversal, providing video, internet, voice, wireless, and entertainment services to residential and business customers. Comcast publishes a public developer program centered on the Firebolt application platform for connected TV experiences, along with authentication and content ingest endpoints used by NBCUniversal media partners. The Firebolt SDK family is used by app developers to write apps once and deploy across Xfinity X1, Xfinity Flex, Sky Q, and other Comcast set-top boxes and connected devices.
finops:
- name: Comcast Finops
  service_category: Telecommunications
  slug: comcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comcast.png
layout: provider
modified: '2026-09-05'
name: Comcast
nav: Providers
network: true
overview: 'Comcast publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cable, Connected Devices, Entertainment, Internet, and Media.


  Comcast''s developer surface includes GitHub presence, privacy policy, documentation, API reference, getting-started guide, support, signup flow, and 33 more developer resources.'
plans:
- name: Comcast Plans Pricing
  plan_count: 0
  slug: comcast-plans-pricing
press:
- date: '2026-05-25'
  title: How Comcast Used AI and Unified Search to Transform ...
  url: https://www.coveo.com/blog/comcast-employee-experience/
- date: '2026-05-25'
  title: Comcast Technology Solutions' VideoAI™ Integrated with ...
  url: https://www.prnewswire.com/news-releases/comcast-technology-solutions-videoai-integrated-with-orange-logic-marketplace-for-ai-powered-management-of-video-assets-and-metadata-302448471.html
- date: '2026-05-25'
  title: Comcast Pushes AI to the Edge to Power the Nation's ...
  url: https://corporate.comcast.com/press/releases/comcast-pushes-ai-to-the-edge-to-power-the-nations-smartest-broadband-network
- date: '2026-05-25'
  title: Comcast Advertising Introduces New AI Platform to Help ...
  url: https://comcastadvertising.com/news/comcast-advertising-introduces-new-ai-platform-to-help-small-and-local-businesses-create-cost-effective-commercials-in-minutes/
- date: '2026-05-25'
  title: 'Comcast''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/comcast-ai-strategy-analysis-of-dominance-in-telecommunications-and-media/
random_paper: 11
rate_limits:
- limit_count: 0
  name: Comcast Rate Limits
  slug: comcast-rate-limits
scopes:
- name: Comcast Scopes
  scope_count: 0
  slug: comcast-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 17.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/comcast/refs/heads/main/screenshots/comcast-2026-06-20T174802.png
security:
- kind: authentication
  name: Comcast Authentication
  slug: comcast-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Comcast Domain Security
  slug: comcast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Comcast Vulnerability Disclosure
  slug: comcast-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: comcast
tags:
- Cable
- Connected Devices
- Entertainment
- Internet
- Media
- Mobile
- Streaming
- Wireless
- Fortune 100
website: https://www.comcast.com
---
