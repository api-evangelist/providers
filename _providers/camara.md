---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Camara Agentic Access
  operation_count: 5
  slug: camara-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 11
apis:
- description: Provides location-verification, location-retrieval, and geofencing subscription endpoints allowing applications to confirm whether a mobile device is in a specified area, to retrieve the last known ar
  name: CAMARA Device Location API
  slug: device-location-api
- description: Silent, cryptographically strong verification that the mobile number a user claims to own is actually the number of the SIM attached to the device making the request. Replaces SMS one-time-password fl
  name: CAMARA Number Verification API
  slug: number-verification-api
- description: Detects whether the SIM attached to a given mobile number has recently been changed. Used by banks, crypto platforms, and other high-assurance services to mitigate SIM-swap account-takeover attacks be
  name: CAMARA SIM Swap API
  slug: sim-swap-api
- description: Provides queries and event subscriptions about a mobile device's connectivity status (reachable, connected, roaming) so applications can adapt behaviour, trigger retries, or switch channels based on r
  name: CAMARA Device Status API
  slug: device-status-api
- description: Returns the closest Mobile Edge Cloud (MEC) endpoint for a given device based on operator network topology, allowing edge-native applications to connect to the lowest-latency edge zone without embeddi
  name: CAMARA Simple Edge Discovery API
  slug: simple-edge-discovery-api
- description: Lifecycle APIs for deploying, managing, and terminating edge-native application instances across operator Mobile Edge Cloud infrastructure, enabling developers to place workloads close to end users wi
  name: CAMARA Edge Application Management API
  slug: edge-application-management-api
- description: Returns a privacy-preserving identifier for a device associated with a network-attached session, enabling correlation and authentication flows while minimising exposure of raw MSISDNs or IMEIs.
  name: CAMARA Device Identifier API
  slug: device-identifier-api
- description: Extends Quality On Demand semantics to fixed-line / home broadband devices, allowing applications to request guaranteed bandwidth or low-latency sessions for devices attached to a home gateway.
  name: CAMARA Home Devices Quality On Demand API
  slug: home-devices-qod-api
- description: Exposes network insight data such as historical and real-time network quality, congestion, and throughput characteristics for a subscriber context, letting applications tune streaming, uploads, and sy
  name: CAMARA Connectivity Insights API
  slug: connectivity-insights-api
- description: Shared authorization and consent model across CAMARA APIs, built on OAuth 2.0 / OpenID Connect Client-Initiated Backchannel Authentication (CIBA) so subscribers explicitly consent to application use o
  name: CAMARA Identity and Consent Management API
  slug: identity-and-consent-management-api
- baseURL: https://api.example.com/quality-on-demand/v0
  baseurl_source: declared
  description: The Sessions API from CAMARA — 4 operation(s) for sessions.
  name: CAMARA Sessions API
  slug: camara-sessions-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CAMARA Quality On Demand Sessions API
  slug: open-camara-sessions-api
- collection_type: open
  name: CAMARA Quality On Demand API
  slug: open-camara
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/camaraproject/DeviceLocation/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/camaraproject/DeviceLocation/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/camaraproject/DeviceLocation/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camara-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camara-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camara-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/camara-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/camara-project
- group: company
  title: ''
  type: Website
  url: https://camaraproject.org/
- group: docs
  title: ''
  type: Documentation
  url: https://camaraproject.org/apis/
- group: other
  title: ''
  type: Portfolio
  url: https://camaraproject.github.io/releases/portfolio.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/camaraproject
- group: other
  title: ''
  type: Governance
  url: https://github.com/camaraproject/Governance
- group: other
  title: ''
  type: Commonalities
  url: https://github.com/camaraproject/Commonalities
- group: operate
  title: ''
  type: ReleaseManagement
  url: https://github.com/camaraproject/ReleaseManagement
- group: other
  title: ''
  type: LinuxFoundationProject
  url: https://lfnetworking.org/projects/camara/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/camara-context.jsonld
- group: design
  title: ''
  type: VocabularyDefinition
  url: vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: spectral/camara.spectral.yml
- group: company
  title: ''
  type: Blog
  url: https://camaraproject.org/feed/
created: '2026-03-16'
description: CAMARA is an open-source Linux Foundation project developing standardized, open, and globally-available telecom APIs as part of the Telco Global API Alliance. Founded and supported by AT&T, Deutsche Telekom, Ericsson, Google Cloud, Microsoft, Nokia, Telefonica, Vodafone, GSMA, and many others, CAMARA defines consistent, operator-agnostic network capability APIs so developers can access programmable network services such as quality-on-demand, device location, SIM swap, number verification, and edge cloud across multiple carriers through a single, unified, standard API surface.
finops:
- name: Camara Finops
  service_category: API
  slug: camara-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camara.png
jsonld:
- class_count: 0
  name: Camara Context
  property_count: 9
  slug: camara-context
layout: provider
modified: '2026-05-19'
name: CAMARA
nav: Providers
network: true
overview: 'CAMARA publishes 1 API on the [APIs.io](https://apis.io/) network: Sessions API. Tagged areas include Telecom, Network APIs, Standards, Linux Foundation, and Open Gateway.


  The CAMARA catalog on APIs.io includes 1 JSON-LD context.


  CAMARA''s developer surface includes authentication, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Camara Plans Pricing
  plan_count: 3
  slug: camara-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Camara Rate Limits
  slug: camara-rate-limits
scopes:
- name: Camara Scopes
  scope_count: 1
  slug: camara-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 3.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 23.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 47.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camara/refs/heads/main/screenshots/camara-2026-06-20T173901.png
security:
- kind: authentication
  name: Camara Authentication
  slug: camara-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Camara Domain Security
  slug: camara-domain-security
  summary_line: TLSv1.3 · HSTS
slug: camara
tags:
- Telecom
- Network APIs
- Standards
- Linux Foundation
- Open Gateway
- GSMA
- Connectivity
- 5G
website: https://camaraproject.org/
---
