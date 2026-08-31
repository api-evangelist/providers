---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Client SDK and hosted spatial audio server for embedding real-time positional voice in web and native apps. Auth is a connection JWT signed with the developer''s App Secret. The hosted server has been '
  name: High Fidelity Spatial Audio API
  slug: high-fidelity-spatial-audio-api
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/highfidelity/hifi-spatial-audio-js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/highfidelity/hifi-spatial-audio-js/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/highfidelity/hifi-spatial-audio-js/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/high-fidelity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/high-fidelity-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/high-fidelity-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/high-fidelity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/high-fidelity-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/high-fidelity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/high-fidelity-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://www.highfidelity.com/api/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/highfidelity
- group: company
  title: ''
  type: Blog
  url: https://www.highfidelity.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.highfidelity.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.highfidelity.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.highfidelity.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.highfidelity.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.highfidelity.com
created: '2026-07-17'
description: High Fidelity provides live spatial audio technology for apps and games. Its Spatial Audio Client Library (hifi-spatial-audio, MIT) lets developers embed realistic positional voice — 3D azimuth/distance transforms, nearfield "whisper" audio, noise reduction, and many simultaneous speakers over the Opus codec — into web and native applications, and previously connected them to a hosted Spatial Audio API server via signed connection JWTs. Apps including Clubhouse, Hubbub, Breakroom, and Soundstage used the technology. The hosted API service has since been discontinued; the SDK remains open source, and the company's active product is Quad, a spatial social platform that recreates physical meeting spaces. High Fidelity was founded by Philip Rosedale and is a portfolio company of GV.
image: https://raw.githubusercontent.com/highfidelity/hifi-spatial-audio-js/main/utilities/spatialAudioLogo.svg
layout: provider
modified: '2026-07-19'
name: High Fidelity
nav: Providers
network: true
overview: 'High Fidelity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Spatial Audio, Audio, and Voice.


  High Fidelity''s developer surface includes authentication, changelog, getting-started guide, engineering blog, support, pricing, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 23.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/high-fidelity/refs/heads/main/screenshots/high-fidelity-2026-07-25T221150.png
security:
- kind: authentication
  name: High Fidelity Authentication
  slug: high-fidelity-authentication
  summary_line: jwt · 1 scheme
- kind: domain-security
  name: High Fidelity Domain Security
  slug: high-fidelity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: high-fidelity
tags:
- Company
- Consumer
- Spatial Audio
- Audio
- Voice
- WebRTC
- SDK
- Real-Time Communication
- Gaming
website: https://www.highfidelity.com
---
