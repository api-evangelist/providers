---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 187
  human_in_the_loop: 6
  name: Deutsche Telekom Agentic Access
  operation_count: 366
  slug: deutsche-telekom-agentic-access
  summary_line: 366 operations · 187 acting · 6 human-in-the-loop
api_count: 8
apis:
- description: Programmatically send and receive text messages in practically every country through Deutsche Telekom's CPaaS platform (built in partnership with Vonage). Part of the MagentaBusiness API portfolio.
  name: Deutsche Telekom SMS API
  slug: sms-api
- description: Improve customer experience using Rich Communication Services for branded, interactive messaging that extends beyond SMS with media, carousels, and verified sender identity.
  name: Deutsche Telekom Rich Communication Services API
  slug: rcs-api
- description: Transform customer communications with intelligent conversational marketing across messaging channels, integrating bots, agents, and rich media into a single conversational flow.
  name: Deutsche Telekom Conversational Connect API
  slug: conversational-connect-api
- description: Deliver high-quality voice experiences over the low-latency, feature-rich, global Deutsche Telekom network — programmable inbound, outbound, and in-app calling with global reach.
  name: Deutsche Telekom Voice API
  slug: voice-api
- description: Bring people together globally through fully programmable, customizable, live video sessions embedded in applications, including multi-party meetings, screen sharing, and recording.
  name: Deutsche Telekom Video API
  slug: video-api
- description: Programmatic access to communications usage data, delivery reports, and billing breakdowns across the CPaaS portfolio for analytics, reconciliation, and customer dashboards.
  name: Deutsche Telekom Reports API
  slug: reports-api
- description: Build conversational customer experiences in natural language across SMS, RCS, voice, video, and chat channels using Deutsche Telekom's hosted AI Studio tooling.
  name: Deutsche Telekom AI Studio
  slug: ai-studio
- description: Seamless silent verification of a mobile phone number directly through the mobile network — authentication without SMS-based one-time passwords. Aligned with the CAMARA Network API initiative and offe
  name: Deutsche Telekom Number Verification API
  slug: number-verify-api
- description: Easily validate customers with two-factor authentication across multiple channels (SMS, voice, push) backed by Deutsche Telekom's mobile network signaling.
  name: Deutsche Telekom Verify API
  slug: verify-api
- description: Programmatic access to 5G network slicing so application developers can request guaranteed quality of service (latency, throughput) for specific traffic flows over Deutsche Telekom's 5G standalone net
  name: Deutsche Telekom 5G Slices for App Developers
  slug: 5g-slices-api
- description: Open Telekom Cloud (OTC) is T-Systems' GAIA-X-aligned, OpenStack-based public cloud operated from Germany. Offers compute, storage, networking, database, container, AI, and API Gateway services with f
  name: Open Telekom Cloud
  slug: open-telekom-cloud
- description: Cloud-native, ubiquitous enterprise integration platform open-sourced by Deutsche Telekom. Combines a Kong-based API gateway, the Jumper sidecar, Keycloak identity, and the TARDIS control plane to pro
  name: Open Telekom Integration Platform
  slug: open-telekom-integration-platform
- baseURL_template: https://{host}/rover/v3
  baseurl_source: spec_template
  description: The ApiChangelog API from Deutsche Telekom — 3 operation(s) for apichangelog.
  name: Deutsche Telekom ApiChangelog API
  slug: deutsche-telekom-apichangelog-api
- baseURL: https://api.telekom.de/stargate/v2
  baseurl_source: spec
  description: With an ApiExposure you can define and API you want to expose on TARDIS, to provide it to other consumers. It is only possible to expose the entire API. It is not possible to expose a single resource.
  name: Deutsche Telekom ApiExposure API
  slug: deutsche-telekom-apiexposure-api
- baseURL_template: https://{host}/rover/v3
  baseurl_source: spec_template
  description: Manage ApiRoadmaps
  name: Deutsche Telekom ApiRoadmap API
  slug: deutsche-telekom-apiroadmap-api
- baseURL_template: https://{host}/rover/v3
  baseurl_source: spec_template
  description: Manage ApiSpecifications
  name: Deutsche Telekom ApiSpecification API
  slug: deutsche-telekom-apispecification-api
- baseURL: https://api.telekom.de/stargate/v2
  baseurl_source: spec
  description: After an API is successful subscribed, you are able to use the API. It is only possible to subscribe to the entire API. It is not possible to subscribe only to a single resource
  name: Deutsche Telekom ApiSubscription API
  slug: deutsche-telekom-apisubscription-api
- baseURL: https://api.telekom.de/application/v2
  baseurl_source: spec
  description: Manage applications
  name: Deutsche Telekom Application API
  slug: deutsche-telekom-application-api
- description: The Attack Detection API from Deutsche Telekom — 2 operation(s) for attack detection.
  name: Deutsche Telekom Attack Detection API
  slug: deutsche-telekom-attack-detection-api
- description: The Authentication Management API from Deutsche Telekom — 24 operation(s) for authentication management.
  name: Deutsche Telekom Authentication Management API
  slug: deutsche-telekom-authentication-management-api
- description: The Client Attribute Certificate API from Deutsche Telekom — 6 operation(s) for client attribute certificate.
  name: Deutsche Telekom Client Attribute Certificate API
  slug: deutsche-telekom-client-attribute-certificate-api
- description: The Client Initial Access API from Deutsche Telekom — 2 operation(s) for client initial access.
  name: Deutsche Telekom Client Initial Access API
  slug: deutsche-telekom-client-initial-access-api
- description: The Client Registration Policy API from Deutsche Telekom — 1 operation(s) for client registration policy.
  name: Deutsche Telekom Client Registration Policy API
  slug: deutsche-telekom-client-registration-policy-api
- description: The Client Role Mappings API from Deutsche Telekom — 6 operation(s) for client role mappings.
  name: Deutsche Telekom Client Role Mappings API
  slug: deutsche-telekom-client-role-mappings-api
- description: The Client Scopes API from Deutsche Telekom — 2 operation(s) for client scopes.
  name: Deutsche Telekom Client Scopes API
  slug: deutsche-telekom-client-scopes-api
- description: The Clients API from Deutsche Telekom — 24 operation(s) for clients.
  name: Deutsche Telekom Clients API
  slug: deutsche-telekom-clients-api
- description: The Component API from Deutsche Telekom — 3 operation(s) for component.
  name: Deutsche Telekom Component API
  slug: deutsche-telekom-component-api
- baseURL: https://locahost:8080
  baseurl_source: spec
  description: The deleting API from Deutsche Telekom — 1 operation(s) for deleting.
  name: Deutsche Telekom deleting API
  slug: deutsche-telekom-deleting-api
- baseURL: https://locahost:8080
  baseurl_source: spec
  description: An endpoint to download existing files
  name: Deutsche Telekom downloading API
  slug: deutsche-telekom-downloading-api
- baseURL: https://api.telekom.de/event/v2
  baseurl_source: spec
  description: With an EventExposure you declare that your application publishes events of a specific type. This makes the events available for subscription by other applications. Each exposure is scoped to a zone a
  name: Deutsche Telekom EventExposure API
  slug: deutsche-telekom-eventexposure-api
- baseURL_template: https://{host}/rover/v3
  baseurl_source: spec_template
  description: Manage EventSpecifications
  name: Deutsche Telekom EventSpecification API
  slug: deutsche-telekom-eventspecification-api
- baseURL: https://api.telekom.de/event/v2
  baseurl_source: spec
  description: An EventSubscription declares that your application wants to receive events of a specific type. You can configure the delivery mechanism (callback or server-sent events), payload format, and subscribe
  name: Deutsche Telekom EventSubscription API
  slug: deutsche-telekom-eventsubscription-api
- baseURL: https://api.telekom.de/event/v2
  baseurl_source: spec
  description: An EventType is a registry entry representing a known event type. It serves as the canonical reference that both EventExposures and EventSubscriptions point to. EventTypes are identified by a dot-sepa
  name: Deutsche Telekom EventType API
  slug: deutsche-telekom-eventtype-api
- description: The Groups API from Deutsche Telekom — 6 operation(s) for groups.
  name: Deutsche Telekom Groups API
  slug: deutsche-telekom-groups-api
- description: The Identity Providers API from Deutsche Telekom — 9 operation(s) for identity providers.
  name: Deutsche Telekom Identity Providers API
  slug: deutsche-telekom-identity-providers-api
- description: The Key API from Deutsche Telekom — 1 operation(s) for key.
  name: Deutsche Telekom Key API
  slug: deutsche-telekom-key-api
- baseURL: https://locahost:8080
  baseurl_source: spec
  description: The onboarding API from Deutsche Telekom — 3 operation(s) for onboarding.
  name: Deutsche Telekom onboarding API
  slug: deutsche-telekom-onboarding-api
- description: The Protocol Mappers API from Deutsche Telekom — 8 operation(s) for protocol mappers.
  name: Deutsche Telekom Protocol Mappers API
  slug: deutsche-telekom-protocol-mappers-api
- description: The Realms Admin API from Deutsche Telekom — 28 operation(s) for realms admin.
  name: Deutsche Telekom Realms Admin API
  slug: deutsche-telekom-realms-admin-api
- baseURL: https://api.telekom.de/controlplane/v1
  baseurl_source: spec
  description: Manage remoteSubscriptions
  name: Deutsche Telekom RemoteSubscription API
  slug: deutsche-telekom-remotesubscription-api
- description: The Role Mapper API from Deutsche Telekom — 8 operation(s) for role mapper.
  name: Deutsche Telekom Role Mapper API
  slug: deutsche-telekom-role-mapper-api
- description: The Roles API from Deutsche Telekom — 16 operation(s) for roles.
  name: Deutsche Telekom Roles API
  slug: deutsche-telekom-roles-api
- description: The Roles (by ID) API from Deutsche Telekom — 5 operation(s) for roles (by id).
  name: Deutsche Telekom Roles (by ID) API
  slug: deutsche-telekom-roles-by-id-api
- description: The Root API from Deutsche Telekom — 1 operation(s) for root.
  name: Deutsche Telekom Root API
  slug: deutsche-telekom-root-api
- baseURL_template: https://{host}/rover/v3
  baseurl_source: spec_template
  description: Manage Rovers
  name: Deutsche Telekom Rover API
  slug: deutsche-telekom-rover-api
- description: The Scope Mappings API from Deutsche Telekom — 14 operation(s) for scope mappings.
  name: Deutsche Telekom Scope Mappings API
  slug: deutsche-telekom-scope-mappings-api
- baseURL: https://locahost:8080
  baseurl_source: spec
  description: Everything regarding storing and resolving secrets
  name: Deutsche Telekom secrets API
  slug: deutsche-telekom-secrets-api
- baseURL: https://locahost:8080
  baseurl_source: spec
  description: An endpoint to upload new files
  name: Deutsche Telekom uploading API
  slug: deutsche-telekom-uploading-api
- description: The User Storage Provider API from Deutsche Telekom — 6 operation(s) for user storage provider.
  name: Deutsche Telekom User Storage Provider API
  slug: deutsche-telekom-user-storage-provider-api
- description: The Users API from Deutsche Telekom — 24 operation(s) for users.
  name: Deutsche Telekom Users API
  slug: deutsche-telekom-users-api
artifact_total: 115
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Controlplane Api
  slug: open-controlplane-cpapi
- collection_type: open
  name: Application Api
  slug: open-controlplane-discovery-application
- collection_type: open
  name: Event Api
  slug: open-controlplane-discovery-event
- collection_type: open
  name: Stargate Api
  slug: open-controlplane-discovery-stargate
- collection_type: open
  name: File manager API
  slug: open-controlplane-file-manager
- collection_type: open
  name: Keycloak Admin REST API
  slug: open-controlplane-identity
- collection_type: open
  name: Rover Api
  slug: open-controlplane-rover-server
- collection_type: open
  name: Secret Manager API
  slug: open-controlplane-secret-manager
- collection_type: open
  name: Controlplane Api ApiChangelog API
  slug: open-deutsche-telekom-apichangelog-api
- collection_type: open
  name: Controlplane Api ApiChangelog ApiExposure API
  slug: open-deutsche-telekom-apiexposure-api
- collection_type: open
  name: Controlplane Api ApiChangelog ApiRoadmap API
  slug: open-deutsche-telekom-apiroadmap-api
- collection_type: open
  name: Controlplane Api ApiChangelog ApiSpecification API
  slug: open-deutsche-telekom-apispecification-api
- collection_type: open
  name: Controlplane Api ApiChangelog ApiSubscription API
  slug: open-deutsche-telekom-apisubscription-api
- collection_type: open
  name: Controlplane Api ApiChangelog Application API
  slug: open-deutsche-telekom-application-api
- collection_type: open
  name: Controlplane Api ApiChangelog Attack Detection API
  slug: open-deutsche-telekom-attack-detection-api
- collection_type: open
  name: Controlplane Api ApiChangelog Authentication Management API
  slug: open-deutsche-telekom-authentication-management-api
- collection_type: open
  name: Controlplane Api ApiChangelog Client Attribute Certificate API
  slug: open-deutsche-telekom-client-attribute-certificate-api
- collection_type: open
  name: Controlplane Api ApiChangelog Client Initial Access API
  slug: open-deutsche-telekom-client-initial-access-api
- collection_type: open
  name: Controlplane Api ApiChangelog Client Registration Policy API
  slug: open-deutsche-telekom-client-registration-policy-api
- collection_type: open
  name: Controlplane Api ApiChangelog Client Role Mappings API
  slug: open-deutsche-telekom-client-role-mappings-api
- collection_type: open
  name: Controlplane Api ApiChangelog Client Scopes API
  slug: open-deutsche-telekom-client-scopes-api
- collection_type: open
  name: Controlplane Api ApiChangelog Clients API
  slug: open-deutsche-telekom-clients-api
- collection_type: open
  name: Controlplane Api ApiChangelog Component API
  slug: open-deutsche-telekom-component-api
- collection_type: open
  name: Controlplane Api ApiChangelog deleting API
  slug: open-deutsche-telekom-deleting-api
- collection_type: open
  name: Controlplane Api ApiChangelog downloading API
  slug: open-deutsche-telekom-downloading-api
- collection_type: open
  name: Controlplane Api ApiChangelog EventExposure API
  slug: open-deutsche-telekom-eventexposure-api
- collection_type: open
  name: Controlplane Api ApiChangelog EventSpecification API
  slug: open-deutsche-telekom-eventspecification-api
- collection_type: open
  name: Controlplane Api ApiChangelog EventSubscription API
  slug: open-deutsche-telekom-eventsubscription-api
- collection_type: open
  name: Controlplane Api ApiChangelog EventType API
  slug: open-deutsche-telekom-eventtype-api
- collection_type: open
  name: Controlplane Api ApiChangelog Groups API
  slug: open-deutsche-telekom-groups-api
- collection_type: open
  name: Controlplane Api ApiChangelog Identity Providers API
  slug: open-deutsche-telekom-identity-providers-api
- collection_type: open
  name: Controlplane Api ApiChangelog Key API
  slug: open-deutsche-telekom-key-api
- collection_type: open
  name: Controlplane Api ApiChangelog onboarding API
  slug: open-deutsche-telekom-onboarding-api
- collection_type: open
  name: Controlplane Api ApiChangelog Protocol Mappers API
  slug: open-deutsche-telekom-protocol-mappers-api
- collection_type: open
  name: Controlplane Api ApiChangelog Realms Admin API
  slug: open-deutsche-telekom-realms-admin-api
- collection_type: open
  name: Controlplane Api ApiChangelog RemoteSubscription API
  slug: open-deutsche-telekom-remotesubscription-api
- collection_type: open
  name: Controlplane Api ApiChangelog Role Mapper API
  slug: open-deutsche-telekom-role-mapper-api
- collection_type: open
  name: Controlplane Api ApiChangelog Roles API
  slug: open-deutsche-telekom-roles-api
- collection_type: open
  name: Controlplane Api ApiChangelog Roles (by ID) API
  slug: open-deutsche-telekom-roles-by-id-api
- collection_type: open
  name: Controlplane Api ApiChangelog Root API
  slug: open-deutsche-telekom-root-api
- collection_type: open
  name: Controlplane Api ApiChangelog Rover API
  slug: open-deutsche-telekom-rover-api
- collection_type: open
  name: Controlplane Api ApiChangelog Scope Mappings API
  slug: open-deutsche-telekom-scope-mappings-api
- collection_type: open
  name: Controlplane Api ApiChangelog secrets API
  slug: open-deutsche-telekom-secrets-api
- collection_type: open
  name: Controlplane Api ApiChangelog uploading API
  slug: open-deutsche-telekom-uploading-api
- collection_type: open
  name: Controlplane Api ApiChangelog User Storage Provider API
  slug: open-deutsche-telekom-user-storage-provider-api
- collection_type: open
  name: Controlplane Api ApiChangelog Users API
  slug: open-deutsche-telekom-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/deutsche-telekom-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/telekom/controlplane/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/telekom/controlplane/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/telekom/controlplane/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/telekom/controlplane/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deutsche-telekom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-telekom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deutsche-telekom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deutsche-telekom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deutsche-telekom-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.telekom.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.telekom.com/en
- group: start
  title: ''
  type: APIPortal
  url: https://developer.telekom.com/en/api-portal
- group: other
  title: ''
  type: Products
  url: https://developer.telekom.com/en/products
- group: start
  title: ''
  type: InternalDeveloperPortal
  url: https://developer.telekom.de/
- group: other
  title: ''
  type: Catalog
  url: https://developer.telekom.de/catalog
- group: other
  title: ''
  type: OpenTelekomCloud
  url: https://www.open-telekom-cloud.com/en
- group: docs
  title: ''
  type: OpenTelekomCloudDocs
  url: https://docs.otc.t-systems.com/
- group: other
  title: ''
  type: TSystems
  url: https://www.t-systems.com/
- group: other
  title: ''
  type: TMobileUS
  url: https://www.t-mobile.com/
- group: other
  title: ''
  type: Company
  url: https://www.telekom.com/en/company
- group: company
  title: ''
  type: Newsroom
  url: https://www.telekom.com/en/media
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.telekom.com/en/investor-relations
- group: company
  title: ''
  type: Careers
  url: https://www.telekom.com/en/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telekom
- group: build
  title: ''
  type: GitHubOpenSource
  url: https://www.telekom.com/en/corporate-responsibility/digital-responsibility/details/open-source
- group: operate
  title: ''
  type: ContactOpenSource
  url: mailto:opensource@telekom.de
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/deutschetelekom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deutsche-telekom/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@deutschetelekom
- group: docs
  title: ''
  type: Documentation
  url: https://developer.telekom.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.telekom.com/en/api-portal
- group: company
  title: ''
  type: Partner
  url: https://www.vonage.com/communications-apis/
- group: other
  title: ''
  type: OpenGateway
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: other
  title: ''
  type: CAMARA
  url: https://camaraproject.org/
- group: company
  title: ''
  type: Blog
  url: https://developer.telekom.com/en/news
created: '2026-05-25'
description: Deutsche Telekom AG is Europe's largest telecommunications operator, headquartered in Bonn, Germany, serving more than 250 million mobile customers across 50+ countries. It is the parent company of T-Mobile US (NASDAQ TMUS) and the majority owner of T-Systems International, its enterprise IT and cloud arm. For developers, Deutsche Telekom operates a public developer portal at developer.telekom.com offering a MagentaBusiness CPaaS suite (SMS, RCS, Voice, Video, Conversational Connect, Reports, AI Studio) built in partnership with Vonage, plus a growing portfolio of GSMA Open Gateway / CAMARA-aligned Network APIs (Number Verification, Verify, 5G Slices) launched jointly with T-Mobile US. T-Systems operates Open Telekom Cloud, an OpenStack-based sovereign public cloud with full REST APIs across compute, storage, networking, container, database, AI, and API Gateway services. Deutsche Telekom is also a substantial open-source contributor — its github.com/telekom organization publishes
  245+ repositories including the Open Telekom Integration Platform (O28M), the TARDIS control-plane suite (with OpenAPI 3 specs for Rover, Controlplane, Identity, Discovery, File Manager, Secret Manager, and Stargate), the Horizon pub/sub event-streaming ecosystem, the Scale design system, Wurzel RAG ETL framework, and Kubernetes-native networking and IPAM operators.
features:
- MagentaBusiness CPaaS portfolio — SMS, RCS, Voice, Video, Conversational Connect, Reports, and AI Studio delivered in partnership with Vonage
- GSMA Open Gateway / CAMARA-aligned Network APIs — Number Verification and Verify launched jointly with T-Mobile US across Germany and the United States
- 5G network capability APIs including 5G Slices for App Developers and 5G Live Video Production reserved bandwidth services
- Open Telekom Cloud — T-Systems' OpenStack-based sovereign public cloud operated from Germany, with full REST APIs covering compute, storage, networking, container, database, AI, and API Gateway services
- Open Telekom Integration Platform (O28M) — open-sourced cloud-native API gateway built on Kong with the Jumper sidecar, Keycloak identity, and the TARDIS control plane
- TARDIS internal developer platform with multiple control-plane APIs (Rover, Controlplane, Identity, Discovery, File Manager, Secret Manager, Stargate) published on GitHub as OpenAPI 3
- Horizon event-streaming ecosystem (Galaxy, Comet, Quasar, Vortex, Cosmoparrot, Golaris) for pub/sub event delivery, circuit breaking, and Kafka-to-MongoDB synchronization
- Sparrow infrastructure-network monitoring tool, K8s-Breakglass privilege-elevation operator, and the Das-Schiff EVPN-to-the-Host network operator
- Scale design system — the digital design system underpinning Telekom products and Magenta-branded experiences
- Wurzel — Python ETL framework for Retrieval-Augmented Generation pipelines powering Telekom's generative AI workloads
- 5G Trace Visualizer for converting protocol traces into SVG sequence diagrams
- Parent of T-Mobile US (NASDAQ: TMUS) and majority owner of T-Systems International
- 245+ public repositories under the github.com/telekom organization with active contributions to Kubernetes, Cluster API, and CNCF projects
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deutsche-telekom.png
layout: provider
modified: '2026-05-25'
name: Deutsche Telekom
nav: Providers
network: true
overview: 'Deutsche Telekom publishes 38 APIs on the [APIs.io](https://apis.io/) network, including ApiChangelog API, ApiExposure API, ApiRoadmap API, and 35 more. Tagged areas include Telecommunications, Telco, Mobile Network Operator, CPaaS, and Network API.


  Deutsche Telekom''s developer surface includes authentication, YouTube channel, documentation, getting-started guide, engineering blog, and 31 more developer resources.'
random_paper: 13
scopes:
- name: Deutsche Telekom Scopes
  scope_count: 13
  slug: deutsche-telekom-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 65.0
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 18.4
      derived: 0
      marker_coverage: 0.0
      total: 38
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 48.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deutsche-telekom/refs/heads/main/screenshots/deutsche-telekom-2026-06-20T175944.png
security:
- kind: authentication
  name: Deutsche Telekom Authentication
  slug: deutsche-telekom-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Deutsche Telekom Domain Security
  slug: deutsche-telekom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Telekom Vulnerability Disclosure
  slug: deutsche-telekom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-telekom
tags:
- Telecommunications
- Telco
- Mobile Network Operator
- CPaaS
- Network API
- 5G
- Cloud
- Identity
- Number Verification
- Open Gateway
- CAMARA
- T-Systems
- T-Mobile
- Magenta
- MagentaBusiness
- API Gateway
- Open-Source
- Germany
- Europe
website: https://www.telekom.com/en
---
