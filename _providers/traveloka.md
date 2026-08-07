---
access_model:
  confidence: high
  label: Partnership + certification required
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - authentication
  - https://developer.travelokapartnersnetwork.com/get-started
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: 'REST API for distribution partners reselling Traveloka accommodation inventory. Covers hotel and room content, rate search and rate re-validation, booking creation, booking retrieval and cancellation '
  name: Traveloka Partners Network (LOKA) v2 Accommodation API
  slug: traveloka-partners-network-loka-v2-accommodation-api
- description: OpenTravel (OTA) 2017B XML connectivity API for channel managers, property-management systems and hotel technology partners. Traveloka hosts the ARI (availability, rates, inventory) and content push e
  name: Traveloka Connect - Connectivity API
  slug: traveloka-connect-connectivity-api
- description: 'Published JSON contract that accommodation suppliers implement on their own infrastructure so Traveloka can search and book against them - the direction of the integration is inverted, with Traveloka '
  name: Traveloka Atlas - Traveloka Specification API
  slug: traveloka-atlas-traveloka-specification-api
artifact_total: 8
asyncapis:
- description: ''
  name: Traveloka Connect Webhooks
  slug: traveloka-connect-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.traveloka.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.travelokapartnersnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.travelokapartnersnetwork.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.travelokapartnersnetwork.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.travelokapartnersnetwork.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.traveloka.com/en-id/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.traveloka.com/en-id/help
- group: company
  title: ''
  type: Blog
  url: https://www.traveloka.com/en-id/explore
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/traveloka
- group: start
  title: ''
  type: SignUp
  url: https://traveloka.sg.larksuite.com/share/base/form/shrlg7CyVohw5GHPRXwt8LdPCCW
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.traveloka.com/en-id/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.traveloka.com/en-id/privacy-notice
- group: auth
  title: ''
  type: Security
  url: security/traveloka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/traveloka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traveloka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traveloka-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/traveloka-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/traveloka-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/traveloka-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/traveloka-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/traveloka-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/traveloka-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/traveloka-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/traveloka-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/traveloka-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/traveloka-connect-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/traveloka-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/traveloka-loka-partner-api-overlay.yaml
created: '2026-08-05'
description: 'Traveloka (Traveloka Services Pte. Ltd.) is a Southeast Asian multi-product online travel agency operating across Indonesia, Thailand, Vietnam, Malaysia, Singapore, the Philippines, Australia, Japan and South Korea, selling flights, hotels and alternative stays, activities (Xperience), trains, cruises, buses, car rental and airport transfers. Its API surface is entirely partner-facing and runs in three distinct programs: the Traveloka Partners Network (LOKA) v2 REST API for distribution partners reselling Traveloka accommodation inventory; Traveloka Connect, an OpenTravel (OTA) 2017B XML connectivity API for channel managers and property-management systems pushing availability, rates and content; and Traveloka Atlas, a published JSON specification that accommodation suppliers implement on their own hosts so Traveloka can search and book against them. All three are approval-gated behind a partnership agreement and certification; none offer self-serve signup.'
image: https://ik.imagekit.io/tvlk/image/imageResource/2024/08/09/1723192761223-35bd6fefad235fbb690b6d79b050343f.png?tr=q-75
layout: provider
modified: '2026-08-05'
name: Traveloka
nav: Providers
network: true
overview: 'Traveloka publishes 2 APIs on the [APIs.io](https://apis.io/) network: Partners Network (LOKA) v2 Accommodation API and Atlas - Traveloka Specification API. Tagged areas include travel, online-travel-agency, accommodation, hotel-booking, and flights.


  The Traveloka catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Traveloka''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 1
  name: Traveloka Rate Limits
  slug: traveloka-rate-limits
score:
  band: developing
  composite: 51.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.2
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Traveloka Authentication
  slug: traveloka-authentication
  summary_line: oauth2/apiKey/http · 0 schemes
- kind: domain-security
  name: Traveloka Domain Security
  slug: traveloka-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Traveloka Vulnerability Disclosure
  slug: traveloka-vulnerability-disclosure
  summary_line: Bugcrowd
slug: traveloka
tags:
- travel
- online-travel-agency
- accommodation
- hotel-booking
- flights
- activities
- hospitality
- distribution
- channel-manager
- opentravel
- southeast-asia
- indonesia
website: https://www.traveloka.com/
---
