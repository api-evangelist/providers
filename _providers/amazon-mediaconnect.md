---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Amazon Mediaconnect Agentic Access
  operation_count: 50
  slug: amazon-mediaconnect-agentic-access
  summary_line: 50 operations · 36 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Bridges API from Amazon MediaConnect — 7 operation(s) for bridges.
  name: Amazon MediaConnect Bridges API
  slug: amazon-mediaconnect-bridges-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Entitlements API from Amazon MediaConnect — 1 operation(s) for entitlements.
  name: Amazon MediaConnect Entitlements API
  slug: amazon-mediaconnect-entitlements-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Flows API from Amazon MediaConnect — 14 operation(s) for flows.
  name: Amazon MediaConnect Flows API
  slug: amazon-mediaconnect-flows-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Gateway Instances API from Amazon MediaConnect — 2 operation(s) for gateway instances.
  name: Amazon MediaConnect Gateway Instances API
  slug: amazon-mediaconnect-gateway-instances-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Gateways API from Amazon MediaConnect — 2 operation(s) for gateways.
  name: Amazon MediaConnect Gateways API
  slug: amazon-mediaconnect-gateways-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Offerings API from Amazon MediaConnect — 2 operation(s) for offerings.
  name: Amazon MediaConnect Offerings API
  slug: amazon-mediaconnect-offerings-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Reservations API from Amazon MediaConnect — 2 operation(s) for reservations.
  name: Amazon MediaConnect Reservations API
  slug: amazon-mediaconnect-reservations-api
- baseURL: https://mediaconnect.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon MediaConnect — 2 operation(s) for tags.
  name: Amazon MediaConnect Tags API
  slug: amazon-mediaconnect-tags-api
artifact_total: 743
collections:
- collection_type: postman
  name: AWS MediaConnect Bridges API
  slug: postman-amazon-mediaconnect-bridges-api
- collection_type: postman
  name: AWS MediaConnect Bridges Entitlements API
  slug: postman-amazon-mediaconnect-entitlements-api
- collection_type: postman
  name: AWS MediaConnect Bridges Flows API
  slug: postman-amazon-mediaconnect-flows-api
- collection_type: postman
  name: AWS MediaConnect Bridges Gateway Instances API
  slug: postman-amazon-mediaconnect-gateway-instances-api
- collection_type: postman
  name: AWS MediaConnect Bridges Gateways API
  slug: postman-amazon-mediaconnect-gateways-api
- collection_type: postman
  name: AWS MediaConnect Bridges Offerings API
  slug: postman-amazon-mediaconnect-offerings-api
- collection_type: postman
  name: AWS MediaConnect Bridges Reservations API
  slug: postman-amazon-mediaconnect-reservations-api
- collection_type: postman
  name: AWS MediaConnect Bridges Tags API
  slug: postman-amazon-mediaconnect-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS MediaConnect Bridges API
  slug: open-amazon-mediaconnect-bridges-api
- collection_type: open
  name: AWS MediaConnect Bridges Entitlements API
  slug: open-amazon-mediaconnect-entitlements-api
- collection_type: open
  name: AWS MediaConnect Bridges Flows API
  slug: open-amazon-mediaconnect-flows-api
- collection_type: open
  name: AWS MediaConnect Bridges Gateway Instances API
  slug: open-amazon-mediaconnect-gateway-instances-api
- collection_type: open
  name: AWS MediaConnect Bridges Gateways API
  slug: open-amazon-mediaconnect-gateways-api
- collection_type: open
  name: AWS MediaConnect Bridges Offerings API
  slug: open-amazon-mediaconnect-offerings-api
- collection_type: open
  name: AWS MediaConnect Bridges Reservations API
  slug: open-amazon-mediaconnect-reservations-api
- collection_type: open
  name: AWS MediaConnect Bridges Tags API
  slug: open-amazon-mediaconnect-tags-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-mediaconnect-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-mediaconnect/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-mediaconnect-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-mediaconnect-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-mediaconnect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-mediaconnect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-mediaconnect-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/mediaconnect/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/mediaconnect/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/media/tag/aws-elemental-mediaconnect/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/mediaconnect/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-mediaconnect-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-mediaconnect-vocabulary.yaml
created: '2026-03-16'
description: AWS Elemental MediaConnect is a high-quality transport service for live video that provides the reliability, security, and visibility customers expect from traditional satellite and fiber services. It enables broadcasters to build live video workflows in the cloud with reliable transport of broadcast-quality content using protocols including Zixi, RIST, SRT, RTP, and RTP with FEC.
examples:
- key_count: 0
  name: Mediaconnect Api __Boolean Example
  slug: mediaconnect-api-__boolean-example
- key_count: 0
  name: Mediaconnect Api __Double Example
  slug: mediaconnect-api-__double-example
- key_count: 0
  name: Mediaconnect Api __Integer Example
  slug: mediaconnect-api-__integer-example
- key_count: 0
  name: Mediaconnect Api __Map Of__String Example
  slug: mediaconnect-api-__map-of__string-example
- key_count: 0
  name: Mediaconnect Api __String Example
  slug: mediaconnect-api-__string-example
- key_count: 3
  name: Mediaconnect Api Add Bridge Flow Source Request Example
  slug: mediaconnect-api-add-bridge-flow-source-request-example
- key_count: 6
  name: Mediaconnect Api Add Bridge Network Output Request Example
  slug: mediaconnect-api-add-bridge-network-output-request-example
- key_count: 5
  name: Mediaconnect Api Add Bridge Network Source Request Example
  slug: mediaconnect-api-add-bridge-network-source-request-example
- key_count: 1
  name: Mediaconnect Api Add Bridge Output Request Example
  slug: mediaconnect-api-add-bridge-output-request-example
- key_count: 1
  name: Mediaconnect Api Add Bridge Outputs Request Example
  slug: mediaconnect-api-add-bridge-outputs-request-example
- key_count: 2
  name: Mediaconnect Api Add Bridge Outputs Response Example
  slug: mediaconnect-api-add-bridge-outputs-response-example
- key_count: 2
  name: Mediaconnect Api Add Bridge Source Request Example
  slug: mediaconnect-api-add-bridge-source-request-example
- key_count: 1
  name: Mediaconnect Api Add Bridge Sources Request Example
  slug: mediaconnect-api-add-bridge-sources-request-example
- key_count: 2
  name: Mediaconnect Api Add Bridge Sources Response Example
  slug: mediaconnect-api-add-bridge-sources-response-example
- key_count: 1
  name: Mediaconnect Api Add Egress Gateway Bridge Request Example
  slug: mediaconnect-api-add-egress-gateway-bridge-request-example
- key_count: 1
  name: Mediaconnect Api Add Flow Media Streams Request Example
  slug: mediaconnect-api-add-flow-media-streams-request-example
- key_count: 2
  name: Mediaconnect Api Add Flow Media Streams Response Example
  slug: mediaconnect-api-add-flow-media-streams-response-example
- key_count: 1
  name: Mediaconnect Api Add Flow Outputs Request Example
  slug: mediaconnect-api-add-flow-outputs-request-example
- key_count: 2
  name: Mediaconnect Api Add Flow Outputs Response Example
  slug: mediaconnect-api-add-flow-outputs-response-example
- key_count: 0
  name: Mediaconnect Api Add Flow Outputs420 Exception Example
  slug: mediaconnect-api-add-flow-outputs420-exception-example
- key_count: 1
  name: Mediaconnect Api Add Flow Sources Request Example
  slug: mediaconnect-api-add-flow-sources-request-example
- key_count: 2
  name: Mediaconnect Api Add Flow Sources Response Example
  slug: mediaconnect-api-add-flow-sources-response-example
- key_count: 1
  name: Mediaconnect Api Add Flow Vpc Interfaces Request Example
  slug: mediaconnect-api-add-flow-vpc-interfaces-request-example
- key_count: 2
  name: Mediaconnect Api Add Flow Vpc Interfaces Response Example
  slug: mediaconnect-api-add-flow-vpc-interfaces-response-example
- key_count: 2
  name: Mediaconnect Api Add Ingress Gateway Bridge Request Example
  slug: mediaconnect-api-add-ingress-gateway-bridge-request-example
- key_count: 2
  name: Mediaconnect Api Add Maintenance Example
  slug: mediaconnect-api-add-maintenance-example
- key_count: 7
  name: Mediaconnect Api Add Media Stream Request Example
  slug: mediaconnect-api-add-media-stream-request-example
- key_count: 15
  name: Mediaconnect Api Add Output Request Example
  slug: mediaconnect-api-add-output-request-example
- key_count: 0
  name: Mediaconnect Api Algorithm Example
  slug: mediaconnect-api-algorithm-example
- key_count: 10
  name: Mediaconnect Api Bridge Example
  slug: mediaconnect-api-bridge-example
- key_count: 3
  name: Mediaconnect Api Bridge Flow Output Example
  slug: mediaconnect-api-bridge-flow-output-example
- key_count: 4
  name: Mediaconnect Api Bridge Flow Source Example
  slug: mediaconnect-api-bridge-flow-source-example
- key_count: 6
  name: Mediaconnect Api Bridge Network Output Example
  slug: mediaconnect-api-bridge-network-output-example
- key_count: 5
  name: Mediaconnect Api Bridge Network Source Example
  slug: mediaconnect-api-bridge-network-source-example
- key_count: 2
  name: Mediaconnect Api Bridge Output Example
  slug: mediaconnect-api-bridge-output-example
- key_count: 0
  name: Mediaconnect Api Bridge Placement Example
  slug: mediaconnect-api-bridge-placement-example
- key_count: 2
  name: Mediaconnect Api Bridge Source Example
  slug: mediaconnect-api-bridge-source-example
- key_count: 0
  name: Mediaconnect Api Bridge State Example
  slug: mediaconnect-api-bridge-state-example
- key_count: 0
  name: Mediaconnect Api Colorimetry Example
  slug: mediaconnect-api-colorimetry-example
- key_count: 0
  name: Mediaconnect Api Connection Status Example
  slug: mediaconnect-api-connection-status-example
- key_count: 7
  name: Mediaconnect Api Create Bridge Request Example
  slug: mediaconnect-api-create-bridge-request-example
- key_count: 1
  name: Mediaconnect Api Create Bridge Response Example
  slug: mediaconnect-api-create-bridge-response-example
- key_count: 0
  name: Mediaconnect Api Create Bridge420 Exception Example
  slug: mediaconnect-api-create-bridge420-exception-example
- key_count: 10
  name: Mediaconnect Api Create Flow Request Example
  slug: mediaconnect-api-create-flow-request-example
- key_count: 1
  name: Mediaconnect Api Create Flow Response Example
  slug: mediaconnect-api-create-flow-response-example
- key_count: 0
  name: Mediaconnect Api Create Flow420 Exception Example
  slug: mediaconnect-api-create-flow420-exception-example
- key_count: 3
  name: Mediaconnect Api Create Gateway Request Example
  slug: mediaconnect-api-create-gateway-request-example
- key_count: 1
  name: Mediaconnect Api Create Gateway Response Example
  slug: mediaconnect-api-create-gateway-response-example
- key_count: 0
  name: Mediaconnect Api Create Gateway420 Exception Example
  slug: mediaconnect-api-create-gateway420-exception-example
- key_count: 0
  name: Mediaconnect Api Delete Bridge Request Example
  slug: mediaconnect-api-delete-bridge-request-example
- key_count: 1
  name: Mediaconnect Api Delete Bridge Response Example
  slug: mediaconnect-api-delete-bridge-response-example
- key_count: 0
  name: Mediaconnect Api Delete Flow Request Example
  slug: mediaconnect-api-delete-flow-request-example
- key_count: 2
  name: Mediaconnect Api Delete Flow Response Example
  slug: mediaconnect-api-delete-flow-response-example
- key_count: 0
  name: Mediaconnect Api Delete Gateway Request Example
  slug: mediaconnect-api-delete-gateway-request-example
- key_count: 1
  name: Mediaconnect Api Delete Gateway Response Example
  slug: mediaconnect-api-delete-gateway-response-example
- key_count: 0
  name: Mediaconnect Api Deregister Gateway Instance Request Example
  slug: mediaconnect-api-deregister-gateway-instance-request-example
- key_count: 2
  name: Mediaconnect Api Deregister Gateway Instance Response Example
  slug: mediaconnect-api-deregister-gateway-instance-response-example
- key_count: 0
  name: Mediaconnect Api Describe Bridge Request Example
  slug: mediaconnect-api-describe-bridge-request-example
- key_count: 1
  name: Mediaconnect Api Describe Bridge Response Example
  slug: mediaconnect-api-describe-bridge-response-example
- key_count: 0
  name: Mediaconnect Api Describe Flow Request Example
  slug: mediaconnect-api-describe-flow-request-example
- key_count: 2
  name: Mediaconnect Api Describe Flow Response Example
  slug: mediaconnect-api-describe-flow-response-example
- key_count: 0
  name: Mediaconnect Api Describe Gateway Instance Request Example
  slug: mediaconnect-api-describe-gateway-instance-request-example
- key_count: 1
  name: Mediaconnect Api Describe Gateway Instance Response Example
  slug: mediaconnect-api-describe-gateway-instance-response-example
- key_count: 0
  name: Mediaconnect Api Describe Gateway Request Example
  slug: mediaconnect-api-describe-gateway-request-example
- key_count: 1
  name: Mediaconnect Api Describe Gateway Response Example
  slug: mediaconnect-api-describe-gateway-response-example
- key_count: 0
  name: Mediaconnect Api Describe Offering Request Example
  slug: mediaconnect-api-describe-offering-request-example
- key_count: 1
  name: Mediaconnect Api Describe Offering Response Example
  slug: mediaconnect-api-describe-offering-response-example
- key_count: 0
  name: Mediaconnect Api Describe Reservation Request Example
  slug: mediaconnect-api-describe-reservation-request-example
- key_count: 1
  name: Mediaconnect Api Describe Reservation Response Example
  slug: mediaconnect-api-describe-reservation-response-example
- key_count: 0
  name: Mediaconnect Api Desired State Example
  slug: mediaconnect-api-desired-state-example
- key_count: 4
  name: Mediaconnect Api Destination Configuration Example
  slug: mediaconnect-api-destination-configuration-example
- key_count: 3
  name: Mediaconnect Api Destination Configuration Request Example
  slug: mediaconnect-api-destination-configuration-request-example
- key_count: 0
  name: Mediaconnect Api Duration Units Example
  slug: mediaconnect-api-duration-units-example
- key_count: 2
  name: Mediaconnect Api Egress Gateway Bridge Example
  slug: mediaconnect-api-egress-gateway-bridge-example
- key_count: 0
  name: Mediaconnect Api Encoder Profile Example
  slug: mediaconnect-api-encoder-profile-example
- key_count: 0
  name: Mediaconnect Api Encoding Name Example
  slug: mediaconnect-api-encoding-name-example
- key_count: 2
  name: Mediaconnect Api Encoding Parameters Example
  slug: mediaconnect-api-encoding-parameters-example
- key_count: 2
  name: Mediaconnect Api Encoding Parameters Request Example
  slug: mediaconnect-api-encoding-parameters-request-example
- key_count: 9
  name: Mediaconnect Api Encryption Example
  slug: mediaconnect-api-encryption-example
- key_count: 7
  name: Mediaconnect Api Entitlement Example
  slug: mediaconnect-api-entitlement-example
- key_count: 0
  name: Mediaconnect Api Entitlement Status Example
  slug: mediaconnect-api-entitlement-status-example
- key_count: 4
  name: Mediaconnect Api Failover Config Example
  slug: mediaconnect-api-failover-config-example
- key_count: 0
  name: Mediaconnect Api Failover Mode Example
  slug: mediaconnect-api-failover-mode-example
- key_count: 14
  name: Mediaconnect Api Flow Example
  slug: mediaconnect-api-flow-example
- key_count: 7
  name: Mediaconnect Api Fmtp Example
  slug: mediaconnect-api-fmtp-example
- key_count: 7
  name: Mediaconnect Api Fmtp Request Example
  slug: mediaconnect-api-fmtp-request-example
- key_count: 2
  name: Mediaconnect Api Gateway Bridge Source Example
  slug: mediaconnect-api-gateway-bridge-source-example
- key_count: 6
  name: Mediaconnect Api Gateway Example
  slug: mediaconnect-api-gateway-example
- key_count: 8
  name: Mediaconnect Api Gateway Instance Example
  slug: mediaconnect-api-gateway-instance-example
- key_count: 2
  name: Mediaconnect Api Gateway Network Example
  slug: mediaconnect-api-gateway-network-example
- key_count: 0
  name: Mediaconnect Api Gateway State Example
  slug: mediaconnect-api-gateway-state-example
- key_count: 6
  name: Mediaconnect Api Grant Entitlement Request Example
  slug: mediaconnect-api-grant-entitlement-request-example
- key_count: 1
  name: Mediaconnect Api Grant Flow Entitlements Request Example
  slug: mediaconnect-api-grant-flow-entitlements-request-example
- key_count: 2
  name: Mediaconnect Api Grant Flow Entitlements Response Example
  slug: mediaconnect-api-grant-flow-entitlements-response-example
- key_count: 0
  name: Mediaconnect Api Grant Flow Entitlements420 Exception Example
  slug: mediaconnect-api-grant-flow-entitlements420-exception-example
- key_count: 3
  name: Mediaconnect Api Ingress Gateway Bridge Example
  slug: mediaconnect-api-ingress-gateway-bridge-example
- key_count: 3
  name: Mediaconnect Api Input Configuration Example
  slug: mediaconnect-api-input-configuration-example
- key_count: 2
  name: Mediaconnect Api Input Configuration Request Example
  slug: mediaconnect-api-input-configuration-request-example
- key_count: 0
  name: Mediaconnect Api Instance State Example
  slug: mediaconnect-api-instance-state-example
- key_count: 1
  name: Mediaconnect Api Interface Example
  slug: mediaconnect-api-interface-example
- key_count: 1
  name: Mediaconnect Api Interface Request Example
  slug: mediaconnect-api-interface-request-example
- key_count: 0
  name: Mediaconnect Api Key Type Example
  slug: mediaconnect-api-key-type-example
- key_count: 0
  name: Mediaconnect Api List Bridges Request Example
  slug: mediaconnect-api-list-bridges-request-example
- key_count: 2
  name: Mediaconnect Api List Bridges Response Example
  slug: mediaconnect-api-list-bridges-response-example
- key_count: 0
  name: Mediaconnect Api List Entitlements Request Example
  slug: mediaconnect-api-list-entitlements-request-example
- key_count: 2
  name: Mediaconnect Api List Entitlements Response Example
  slug: mediaconnect-api-list-entitlements-response-example
- key_count: 0
  name: Mediaconnect Api List Flows Request Example
  slug: mediaconnect-api-list-flows-request-example
- key_count: 2
  name: Mediaconnect Api List Flows Response Example
  slug: mediaconnect-api-list-flows-response-example
- key_count: 0
  name: Mediaconnect Api List Gateway Instances Request Example
  slug: mediaconnect-api-list-gateway-instances-request-example
- key_count: 2
  name: Mediaconnect Api List Gateway Instances Response Example
  slug: mediaconnect-api-list-gateway-instances-response-example
- key_count: 0
  name: Mediaconnect Api List Gateways Request Example
  slug: mediaconnect-api-list-gateways-request-example
- key_count: 2
  name: Mediaconnect Api List Gateways Response Example
  slug: mediaconnect-api-list-gateways-response-example
- key_count: 0
  name: Mediaconnect Api List Offerings Request Example
  slug: mediaconnect-api-list-offerings-request-example
- key_count: 2
  name: Mediaconnect Api List Offerings Response Example
  slug: mediaconnect-api-list-offerings-response-example
- key_count: 0
  name: Mediaconnect Api List Reservations Request Example
  slug: mediaconnect-api-list-reservations-request-example
- key_count: 2
  name: Mediaconnect Api List Reservations Response Example
  slug: mediaconnect-api-list-reservations-response-example
- key_count: 0
  name: Mediaconnect Api List Tags For Resource Request Example
  slug: mediaconnect-api-list-tags-for-resource-request-example
- key_count: 1
  name: Mediaconnect Api List Tags For Resource Response Example
  slug: mediaconnect-api-list-tags-for-resource-response-example
- key_count: 5
  name: Mediaconnect Api Listed Bridge Example
  slug: mediaconnect-api-listed-bridge-example
- key_count: 3
  name: Mediaconnect Api Listed Entitlement Example
  slug: mediaconnect-api-listed-entitlement-example
- key_count: 7
  name: Mediaconnect Api Listed Flow Example
  slug: mediaconnect-api-listed-flow-example
- key_count: 3
  name: Mediaconnect Api Listed Gateway Example
  slug: mediaconnect-api-listed-gateway-example
- key_count: 4
  name: Mediaconnect Api Listed Gateway Instance Example
  slug: mediaconnect-api-listed-gateway-instance-example
- key_count: 0
  name: Mediaconnect Api Maintenance Day Example
  slug: mediaconnect-api-maintenance-day-example
- key_count: 4
  name: Mediaconnect Api Maintenance Example
  slug: mediaconnect-api-maintenance-example
- key_count: 0
  name: Mediaconnect Api Max Results Example
  slug: mediaconnect-api-max-results-example
- key_count: 2
  name: Mediaconnect Api Media Stream Attributes Example
  slug: mediaconnect-api-media-stream-attributes-example
- key_count: 2
  name: Mediaconnect Api Media Stream Attributes Request Example
  slug: mediaconnect-api-media-stream-attributes-request-example
- key_count: 8
  name: Mediaconnect Api Media Stream Example
  slug: mediaconnect-api-media-stream-example
- key_count: 4
  name: Mediaconnect Api Media Stream Output Configuration Example
  slug: mediaconnect-api-media-stream-output-configuration-example
- key_count: 4
  name: Mediaconnect Api Media Stream Output Configuration Request Example
  slug: mediaconnect-api-media-stream-output-configuration-request-example
- key_count: 3
  name: Mediaconnect Api Media Stream Source Configuration Example
  slug: mediaconnect-api-media-stream-source-configuration-example
- key_count: 3
  name: Mediaconnect Api Media Stream Source Configuration Request Example
  slug: mediaconnect-api-media-stream-source-configuration-request-example
- key_count: 0
  name: Mediaconnect Api Media Stream Type Example
  slug: mediaconnect-api-media-stream-type-example
- key_count: 3
  name: Mediaconnect Api Message Detail Example
  slug: mediaconnect-api-message-detail-example
- key_count: 1
  name: Mediaconnect Api Messages Example
  slug: mediaconnect-api-messages-example
- key_count: 0
  name: Mediaconnect Api Network Interface Type Example
  slug: mediaconnect-api-network-interface-type-example
- key_count: 8
  name: Mediaconnect Api Offering Example
  slug: mediaconnect-api-offering-example
- key_count: 15
  name: Mediaconnect Api Output Example
  slug: mediaconnect-api-output-example
- key_count: 0
  name: Mediaconnect Api Price Units Example
  slug: mediaconnect-api-price-units-example
- key_count: 0
  name: Mediaconnect Api Protocol Example
  slug: mediaconnect-api-protocol-example
- key_count: 2
  name: Mediaconnect Api Purchase Offering Request Example
  slug: mediaconnect-api-purchase-offering-request-example
- key_count: 1
  name: Mediaconnect Api Purchase Offering Response Example
  slug: mediaconnect-api-purchase-offering-response-example
- key_count: 0
  name: Mediaconnect Api Range Example
  slug: mediaconnect-api-range-example
- key_count: 0
  name: Mediaconnect Api Remove Bridge Output Request Example
  slug: mediaconnect-api-remove-bridge-output-request-example
- key_count: 2
  name: Mediaconnect Api Remove Bridge Output Response Example
  slug: mediaconnect-api-remove-bridge-output-response-example
- key_count: 0
  name: Mediaconnect Api Remove Bridge Source Request Example
  slug: mediaconnect-api-remove-bridge-source-request-example
- key_count: 2
  name: Mediaconnect Api Remove Bridge Source Response Example
  slug: mediaconnect-api-remove-bridge-source-response-example
- key_count: 0
  name: Mediaconnect Api Remove Flow Media Stream Request Example
  slug: mediaconnect-api-remove-flow-media-stream-request-example
- key_count: 2
  name: Mediaconnect Api Remove Flow Media Stream Response Example
  slug: mediaconnect-api-remove-flow-media-stream-response-example
- key_count: 0
  name: Mediaconnect Api Remove Flow Output Request Example
  slug: mediaconnect-api-remove-flow-output-request-example
- key_count: 2
  name: Mediaconnect Api Remove Flow Output Response Example
  slug: mediaconnect-api-remove-flow-output-response-example
- key_count: 0
  name: Mediaconnect Api Remove Flow Source Request Example
  slug: mediaconnect-api-remove-flow-source-request-example
- key_count: 2
  name: Mediaconnect Api Remove Flow Source Response Example
  slug: mediaconnect-api-remove-flow-source-response-example
- key_count: 0
  name: Mediaconnect Api Remove Flow Vpc Interface Request Example
  slug: mediaconnect-api-remove-flow-vpc-interface-request-example
- key_count: 3
  name: Mediaconnect Api Remove Flow Vpc Interface Response Example
  slug: mediaconnect-api-remove-flow-vpc-interface-response-example
- key_count: 13
  name: Mediaconnect Api Reservation Example
  slug: mediaconnect-api-reservation-example
- key_count: 0
  name: Mediaconnect Api Reservation State Example
  slug: mediaconnect-api-reservation-state-example
- key_count: 2
  name: Mediaconnect Api Resource Specification Example
  slug: mediaconnect-api-resource-specification-example
- key_count: 0
  name: Mediaconnect Api Resource Type Example
  slug: mediaconnect-api-resource-type-example
- key_count: 0
  name: Mediaconnect Api Revoke Flow Entitlement Request Example
  slug: mediaconnect-api-revoke-flow-entitlement-request-example
- key_count: 2
  name: Mediaconnect Api Revoke Flow Entitlement Response Example
  slug: mediaconnect-api-revoke-flow-entitlement-response-example
- key_count: 0
  name: Mediaconnect Api Scan Mode Example
  slug: mediaconnect-api-scan-mode-example
- key_count: 2
  name: Mediaconnect Api Set Gateway Bridge Source Request Example
  slug: mediaconnect-api-set-gateway-bridge-source-request-example
- key_count: 19
  name: Mediaconnect Api Set Source Request Example
  slug: mediaconnect-api-set-source-request-example
- key_count: 15
  name: Mediaconnect Api Source Example
  slug: mediaconnect-api-source-example
- key_count: 1
  name: Mediaconnect Api Source Priority Example
  slug: mediaconnect-api-source-priority-example
- key_count: 0
  name: Mediaconnect Api Source Type Example
  slug: mediaconnect-api-source-type-example
- key_count: 0
  name: Mediaconnect Api Start Flow Request Example
  slug: mediaconnect-api-start-flow-request-example
- key_count: 2
  name: Mediaconnect Api Start Flow Response Example
  slug: mediaconnect-api-start-flow-response-example
- key_count: 0
  name: Mediaconnect Api State Example
  slug: mediaconnect-api-state-example
- key_count: 0
  name: Mediaconnect Api Status Example
  slug: mediaconnect-api-status-example
- key_count: 0
  name: Mediaconnect Api Stop Flow Request Example
  slug: mediaconnect-api-stop-flow-request-example
- key_count: 2
  name: Mediaconnect Api Stop Flow Response Example
  slug: mediaconnect-api-stop-flow-response-example
- key_count: 1
  name: Mediaconnect Api Tag Resource Request Example
  slug: mediaconnect-api-tag-resource-request-example
- key_count: 0
  name: Mediaconnect Api Tcs Example
  slug: mediaconnect-api-tcs-example
- key_count: 13
  name: Mediaconnect Api Transport Example
  slug: mediaconnect-api-transport-example
- key_count: 0
  name: Mediaconnect Api Untag Resource Request Example
  slug: mediaconnect-api-untag-resource-request-example
- key_count: 2
  name: Mediaconnect Api Update Bridge Flow Source Request Example
  slug: mediaconnect-api-update-bridge-flow-source-request-example
- key_count: 5
  name: Mediaconnect Api Update Bridge Network Output Request Example
  slug: mediaconnect-api-update-bridge-network-output-request-example
- key_count: 4
  name: Mediaconnect Api Update Bridge Network Source Request Example
  slug: mediaconnect-api-update-bridge-network-source-request-example
- key_count: 1
  name: Mediaconnect Api Update Bridge Output Request Example
  slug: mediaconnect-api-update-bridge-output-request-example
- key_count: 2
  name: Mediaconnect Api Update Bridge Output Response Example
  slug: mediaconnect-api-update-bridge-output-response-example
- key_count: 3
  name: Mediaconnect Api Update Bridge Request Example
  slug: mediaconnect-api-update-bridge-request-example
- key_count: 1
  name: Mediaconnect Api Update Bridge Response Example
  slug: mediaconnect-api-update-bridge-response-example
- key_count: 2
  name: Mediaconnect Api Update Bridge Source Request Example
  slug: mediaconnect-api-update-bridge-source-request-example
- key_count: 2
  name: Mediaconnect Api Update Bridge Source Response Example
  slug: mediaconnect-api-update-bridge-source-response-example
- key_count: 1
  name: Mediaconnect Api Update Bridge State Request Example
  slug: mediaconnect-api-update-bridge-state-request-example
- key_count: 2
  name: Mediaconnect Api Update Bridge State Response Example
  slug: mediaconnect-api-update-bridge-state-response-example
- key_count: 1
  name: Mediaconnect Api Update Egress Gateway Bridge Request Example
  slug: mediaconnect-api-update-egress-gateway-bridge-request-example
- key_count: 9
  name: Mediaconnect Api Update Encryption Example
  slug: mediaconnect-api-update-encryption-example
- key_count: 4
  name: Mediaconnect Api Update Failover Config Example
  slug: mediaconnect-api-update-failover-config-example
- key_count: 4
  name: Mediaconnect Api Update Flow Entitlement Request Example
  slug: mediaconnect-api-update-flow-entitlement-request-example
- key_count: 2
  name: Mediaconnect Api Update Flow Entitlement Response Example
  slug: mediaconnect-api-update-flow-entitlement-response-example
- key_count: 5
  name: Mediaconnect Api Update Flow Media Stream Request Example
  slug: mediaconnect-api-update-flow-media-stream-request-example
- key_count: 2
  name: Mediaconnect Api Update Flow Media Stream Response Example
  slug: mediaconnect-api-update-flow-media-stream-response-example
- key_count: 15
  name: Mediaconnect Api Update Flow Output Request Example
  slug: mediaconnect-api-update-flow-output-request-example
- key_count: 2
  name: Mediaconnect Api Update Flow Output Response Example
  slug: mediaconnect-api-update-flow-output-response-example
- key_count: 2
  name: Mediaconnect Api Update Flow Request Example
  slug: mediaconnect-api-update-flow-request-example
- key_count: 1
  name: Mediaconnect Api Update Flow Response Example
  slug: mediaconnect-api-update-flow-response-example
- key_count: 18
  name: Mediaconnect Api Update Flow Source Request Example
  slug: mediaconnect-api-update-flow-source-request-example
- key_count: 2
  name: Mediaconnect Api Update Flow Source Response Example
  slug: mediaconnect-api-update-flow-source-response-example
- key_count: 2
  name: Mediaconnect Api Update Gateway Bridge Source Request Example
  slug: mediaconnect-api-update-gateway-bridge-source-request-example
- key_count: 1
  name: Mediaconnect Api Update Gateway Instance Request Example
  slug: mediaconnect-api-update-gateway-instance-request-example
- key_count: 2
  name: Mediaconnect Api Update Gateway Instance Response Example
  slug: mediaconnect-api-update-gateway-instance-response-example
- key_count: 2
  name: Mediaconnect Api Update Ingress Gateway Bridge Request Example
  slug: mediaconnect-api-update-ingress-gateway-bridge-request-example
- key_count: 3
  name: Mediaconnect Api Update Maintenance Example
  slug: mediaconnect-api-update-maintenance-example
- key_count: 1
  name: Mediaconnect Api Vpc Interface Attachment Example
  slug: mediaconnect-api-vpc-interface-attachment-example
- key_count: 6
  name: Mediaconnect Api Vpc Interface Example
  slug: mediaconnect-api-vpc-interface-example
- key_count: 5
  name: Mediaconnect Api Vpc Interface Request Example
  slug: mediaconnect-api-vpc-interface-request-example
features:
- description: Supports Zixi, RIST, SRT, RTP, and RTP with FEC protocols for reliable live video delivery over IP networks.
  name: Video Transport Protocols
- description: Transmit compressed video between on-premises multicast environments and cloud infrastructure via the MediaConnect Gateway.
  name: Gateway Capability
- description: Handle uncompressed and visually-lossless video through AWS CDI and JPEG XS encoding with low-latency delivery.
  name: Uncompressed Video Support
- description: Built-in AES encryption with AWS Secrets Manager integration for encryption key management.
  name: End-to-End Encryption
- description: Grant partner and customer accounts controlled access to your video streams via entitlements.
  name: Entitlements
- description: Programmatically create and manage flows, sources, outputs, and VPC interfaces.
  name: Flow Management
- description: Visualize relationships between resources in live video workflows across connected AWS services.
  name: Workflow Monitor
finops:
- name: Amazon Mediaconnect Finops
  service_category: API
  slug: amazon-mediaconnect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-mediaconnect.png
json_schemas:
- name: __boolean
  property_count: 0
  slug: mediaconnect-api-__boolean
- name: __double
  property_count: 0
  slug: mediaconnect-api-__double
- name: __integer
  property_count: 0
  slug: mediaconnect-api-__integer
- name: __listOfAddBridgeOutputRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-add-bridge-output-request
- name: __listOfAddBridgeSourceRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-add-bridge-source-request
- name: __listOfAddMediaStreamRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-add-media-stream-request
- name: __listOfAddOutputRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-add-output-request
- name: __listOfBridgeOutput
  property_count: 0
  slug: mediaconnect-api-__list-of-bridge-output
- name: __listOfBridgeSource
  property_count: 0
  slug: mediaconnect-api-__list-of-bridge-source
- name: __listOfDestinationConfigurationRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-destination-configuration-request
- name: __listOfDestinationConfiguration
  property_count: 0
  slug: mediaconnect-api-__list-of-destination-configuration
- name: __listOfEntitlement
  property_count: 0
  slug: mediaconnect-api-__list-of-entitlement
- name: __listOfGatewayNetwork
  property_count: 0
  slug: mediaconnect-api-__list-of-gateway-network
- name: __listOfGrantEntitlementRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-grant-entitlement-request
- name: __listOfInputConfigurationRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-input-configuration-request
- name: __listOfInputConfiguration
  property_count: 0
  slug: mediaconnect-api-__list-of-input-configuration
- name: __listOfListedBridge
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-bridge
- name: __listOfListedEntitlement
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-entitlement
- name: __listOfListedFlow
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-flow
- name: __listOfListedGatewayInstance
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-gateway-instance
- name: __listOfListedGateway
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-gateway
- name: __listOfMediaStreamOutputConfigurationRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-output-configuration-request
- name: __listOfMediaStreamOutputConfiguration
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-output-configuration
- name: __listOfMediaStream
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream
- name: __listOfMediaStreamSourceConfigurationRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-source-configuration-request
- name: __listOfMediaStreamSourceConfiguration
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-source-configuration
- name: __listOfMessageDetail
  property_count: 0
  slug: mediaconnect-api-__list-of-message-detail
- name: __listOfOffering
  property_count: 0
  slug: mediaconnect-api-__list-of-offering
- name: __listOfOutput
  property_count: 0
  slug: mediaconnect-api-__list-of-output
- name: __listOfReservation
  property_count: 0
  slug: mediaconnect-api-__list-of-reservation
- name: __listOfSetSourceRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-set-source-request
- name: __listOfSource
  property_count: 0
  slug: mediaconnect-api-__list-of-source
- name: __listOfVpcInterfaceRequest
  property_count: 0
  slug: mediaconnect-api-__list-of-vpc-interface-request
- name: __listOfVpcInterface
  property_count: 0
  slug: mediaconnect-api-__list-of-vpc-interface
- name: __listOf__integer
  property_count: 0
  slug: mediaconnect-api-__list-of__integer
- name: __listOf__string
  property_count: 0
  slug: mediaconnect-api-__list-of__string
- name: __mapOf__string
  property_count: 0
  slug: mediaconnect-api-__map-of__string
- name: __string
  property_count: 0
  slug: mediaconnect-api-__string
- name: AddBridgeFlowSourceRequest
  property_count: 3
  slug: mediaconnect-api-add-bridge-flow-source-request
- name: AddBridgeNetworkOutputRequest
  property_count: 6
  slug: mediaconnect-api-add-bridge-network-output-request
- name: AddBridgeNetworkSourceRequest
  property_count: 5
  slug: mediaconnect-api-add-bridge-network-source-request
- name: AddBridgeOutputRequest
  property_count: 1
  slug: mediaconnect-api-add-bridge-output-request
- name: AddBridgeOutputsRequest
  property_count: 1
  slug: mediaconnect-api-add-bridge-outputs-request
- name: AddBridgeOutputsResponse
  property_count: 2
  slug: mediaconnect-api-add-bridge-outputs-response
- name: AddBridgeSourceRequest
  property_count: 2
  slug: mediaconnect-api-add-bridge-source-request
- name: AddBridgeSourcesRequest
  property_count: 1
  slug: mediaconnect-api-add-bridge-sources-request
- name: AddBridgeSourcesResponse
  property_count: 2
  slug: mediaconnect-api-add-bridge-sources-response
- name: AddEgressGatewayBridgeRequest
  property_count: 1
  slug: mediaconnect-api-add-egress-gateway-bridge-request
- name: AddFlowMediaStreamsRequest
  property_count: 1
  slug: mediaconnect-api-add-flow-media-streams-request
- name: AddFlowMediaStreamsResponse
  property_count: 2
  slug: mediaconnect-api-add-flow-media-streams-response
- name: AddFlowOutputsRequest
  property_count: 1
  slug: mediaconnect-api-add-flow-outputs-request
- name: AddFlowOutputsResponse
  property_count: 2
  slug: mediaconnect-api-add-flow-outputs-response
- name: AddFlowOutputs420Exception
  property_count: 0
  slug: mediaconnect-api-add-flow-outputs420-exception
- name: AddFlowSourcesRequest
  property_count: 1
  slug: mediaconnect-api-add-flow-sources-request
- name: AddFlowSourcesResponse
  property_count: 2
  slug: mediaconnect-api-add-flow-sources-response
- name: AddFlowVpcInterfacesRequest
  property_count: 1
  slug: mediaconnect-api-add-flow-vpc-interfaces-request
- name: AddFlowVpcInterfacesResponse
  property_count: 2
  slug: mediaconnect-api-add-flow-vpc-interfaces-response
- name: AddIngressGatewayBridgeRequest
  property_count: 2
  slug: mediaconnect-api-add-ingress-gateway-bridge-request
- name: AddMaintenance
  property_count: 2
  slug: mediaconnect-api-add-maintenance
- name: AddMediaStreamRequest
  property_count: 7
  slug: mediaconnect-api-add-media-stream-request
- name: AddOutputRequest
  property_count: 15
  slug: mediaconnect-api-add-output-request
- name: Algorithm
  property_count: 0
  slug: mediaconnect-api-algorithm
- name: BridgeFlowOutput
  property_count: 3
  slug: mediaconnect-api-bridge-flow-output
- name: BridgeFlowSource
  property_count: 4
  slug: mediaconnect-api-bridge-flow-source
- name: BridgeNetworkOutput
  property_count: 6
  slug: mediaconnect-api-bridge-network-output
- name: BridgeNetworkSource
  property_count: 5
  slug: mediaconnect-api-bridge-network-source
- name: BridgeOutput
  property_count: 2
  slug: mediaconnect-api-bridge-output
- name: BridgePlacement
  property_count: 0
  slug: mediaconnect-api-bridge-placement
- name: Bridge
  property_count: 10
  slug: mediaconnect-api-bridge
- name: BridgeSource
  property_count: 2
  slug: mediaconnect-api-bridge-source
- name: BridgeState
  property_count: 0
  slug: mediaconnect-api-bridge-state
- name: Colorimetry
  property_count: 0
  slug: mediaconnect-api-colorimetry
- name: ConnectionStatus
  property_count: 0
  slug: mediaconnect-api-connection-status
- name: CreateBridgeRequest
  property_count: 7
  slug: mediaconnect-api-create-bridge-request
- name: CreateBridgeResponse
  property_count: 1
  slug: mediaconnect-api-create-bridge-response
- name: CreateBridge420Exception
  property_count: 0
  slug: mediaconnect-api-create-bridge420-exception
- name: CreateFlowRequest
  property_count: 10
  slug: mediaconnect-api-create-flow-request
- name: CreateFlowResponse
  property_count: 1
  slug: mediaconnect-api-create-flow-response
- name: CreateFlow420Exception
  property_count: 0
  slug: mediaconnect-api-create-flow420-exception
- name: CreateGatewayRequest
  property_count: 3
  slug: mediaconnect-api-create-gateway-request
- name: CreateGatewayResponse
  property_count: 1
  slug: mediaconnect-api-create-gateway-response
- name: CreateGateway420Exception
  property_count: 0
  slug: mediaconnect-api-create-gateway420-exception
- name: DeleteBridgeRequest
  property_count: 0
  slug: mediaconnect-api-delete-bridge-request
- name: DeleteBridgeResponse
  property_count: 1
  slug: mediaconnect-api-delete-bridge-response
- name: DeleteFlowRequest
  property_count: 0
  slug: mediaconnect-api-delete-flow-request
- name: DeleteFlowResponse
  property_count: 2
  slug: mediaconnect-api-delete-flow-response
- name: DeleteGatewayRequest
  property_count: 0
  slug: mediaconnect-api-delete-gateway-request
- name: DeleteGatewayResponse
  property_count: 1
  slug: mediaconnect-api-delete-gateway-response
- name: DeregisterGatewayInstanceRequest
  property_count: 0
  slug: mediaconnect-api-deregister-gateway-instance-request
- name: DeregisterGatewayInstanceResponse
  property_count: 2
  slug: mediaconnect-api-deregister-gateway-instance-response
- name: DescribeBridgeRequest
  property_count: 0
  slug: mediaconnect-api-describe-bridge-request
- name: DescribeBridgeResponse
  property_count: 1
  slug: mediaconnect-api-describe-bridge-response
- name: DescribeFlowRequest
  property_count: 0
  slug: mediaconnect-api-describe-flow-request
- name: DescribeFlowResponse
  property_count: 2
  slug: mediaconnect-api-describe-flow-response
- name: DescribeGatewayInstanceRequest
  property_count: 0
  slug: mediaconnect-api-describe-gateway-instance-request
- name: DescribeGatewayInstanceResponse
  property_count: 1
  slug: mediaconnect-api-describe-gateway-instance-response
- name: DescribeGatewayRequest
  property_count: 0
  slug: mediaconnect-api-describe-gateway-request
- name: DescribeGatewayResponse
  property_count: 1
  slug: mediaconnect-api-describe-gateway-response
- name: DescribeOfferingRequest
  property_count: 0
  slug: mediaconnect-api-describe-offering-request
- name: DescribeOfferingResponse
  property_count: 1
  slug: mediaconnect-api-describe-offering-response
- name: DescribeReservationRequest
  property_count: 0
  slug: mediaconnect-api-describe-reservation-request
- name: DescribeReservationResponse
  property_count: 1
  slug: mediaconnect-api-describe-reservation-response
- name: DesiredState
  property_count: 0
  slug: mediaconnect-api-desired-state
- name: DestinationConfigurationRequest
  property_count: 3
  slug: mediaconnect-api-destination-configuration-request
- name: DestinationConfiguration
  property_count: 4
  slug: mediaconnect-api-destination-configuration
- name: DurationUnits
  property_count: 0
  slug: mediaconnect-api-duration-units
- name: EgressGatewayBridge
  property_count: 2
  slug: mediaconnect-api-egress-gateway-bridge
- name: EncoderProfile
  property_count: 0
  slug: mediaconnect-api-encoder-profile
- name: EncodingName
  property_count: 0
  slug: mediaconnect-api-encoding-name
- name: EncodingParametersRequest
  property_count: 2
  slug: mediaconnect-api-encoding-parameters-request
- name: EncodingParameters
  property_count: 2
  slug: mediaconnect-api-encoding-parameters
- name: Encryption
  property_count: 9
  slug: mediaconnect-api-encryption
- name: Entitlement
  property_count: 7
  slug: mediaconnect-api-entitlement
- name: EntitlementStatus
  property_count: 0
  slug: mediaconnect-api-entitlement-status
- name: FailoverConfig
  property_count: 4
  slug: mediaconnect-api-failover-config
- name: FailoverMode
  property_count: 0
  slug: mediaconnect-api-failover-mode
- name: Flow
  property_count: 14
  slug: mediaconnect-api-flow
- name: FmtpRequest
  property_count: 7
  slug: mediaconnect-api-fmtp-request
- name: Fmtp
  property_count: 7
  slug: mediaconnect-api-fmtp
- name: GatewayBridgeSource
  property_count: 2
  slug: mediaconnect-api-gateway-bridge-source
- name: GatewayInstance
  property_count: 8
  slug: mediaconnect-api-gateway-instance
- name: GatewayNetwork
  property_count: 2
  slug: mediaconnect-api-gateway-network
- name: Gateway
  property_count: 6
  slug: mediaconnect-api-gateway
- name: GatewayState
  property_count: 0
  slug: mediaconnect-api-gateway-state
- name: GrantEntitlementRequest
  property_count: 6
  slug: mediaconnect-api-grant-entitlement-request
- name: GrantFlowEntitlementsRequest
  property_count: 1
  slug: mediaconnect-api-grant-flow-entitlements-request
- name: GrantFlowEntitlementsResponse
  property_count: 2
  slug: mediaconnect-api-grant-flow-entitlements-response
- name: GrantFlowEntitlements420Exception
  property_count: 0
  slug: mediaconnect-api-grant-flow-entitlements420-exception
- name: IngressGatewayBridge
  property_count: 3
  slug: mediaconnect-api-ingress-gateway-bridge
- name: InputConfigurationRequest
  property_count: 2
  slug: mediaconnect-api-input-configuration-request
- name: InputConfiguration
  property_count: 3
  slug: mediaconnect-api-input-configuration
- name: InstanceState
  property_count: 0
  slug: mediaconnect-api-instance-state
- name: InterfaceRequest
  property_count: 1
  slug: mediaconnect-api-interface-request
- name: Interface
  property_count: 1
  slug: mediaconnect-api-interface
- name: KeyType
  property_count: 0
  slug: mediaconnect-api-key-type
- name: ListBridgesRequest
  property_count: 0
  slug: mediaconnect-api-list-bridges-request
- name: ListBridgesResponse
  property_count: 2
  slug: mediaconnect-api-list-bridges-response
- name: ListEntitlementsRequest
  property_count: 0
  slug: mediaconnect-api-list-entitlements-request
- name: ListEntitlementsResponse
  property_count: 2
  slug: mediaconnect-api-list-entitlements-response
- name: ListFlowsRequest
  property_count: 0
  slug: mediaconnect-api-list-flows-request
- name: ListFlowsResponse
  property_count: 2
  slug: mediaconnect-api-list-flows-response
- name: ListGatewayInstancesRequest
  property_count: 0
  slug: mediaconnect-api-list-gateway-instances-request
- name: ListGatewayInstancesResponse
  property_count: 2
  slug: mediaconnect-api-list-gateway-instances-response
- name: ListGatewaysRequest
  property_count: 0
  slug: mediaconnect-api-list-gateways-request
- name: ListGatewaysResponse
  property_count: 2
  slug: mediaconnect-api-list-gateways-response
- name: ListOfferingsRequest
  property_count: 0
  slug: mediaconnect-api-list-offerings-request
- name: ListOfferingsResponse
  property_count: 2
  slug: mediaconnect-api-list-offerings-response
- name: ListReservationsRequest
  property_count: 0
  slug: mediaconnect-api-list-reservations-request
- name: ListReservationsResponse
  property_count: 2
  slug: mediaconnect-api-list-reservations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: mediaconnect-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: mediaconnect-api-list-tags-for-resource-response
- name: ListedBridge
  property_count: 5
  slug: mediaconnect-api-listed-bridge
- name: ListedEntitlement
  property_count: 3
  slug: mediaconnect-api-listed-entitlement
- name: ListedFlow
  property_count: 7
  slug: mediaconnect-api-listed-flow
- name: ListedGatewayInstance
  property_count: 4
  slug: mediaconnect-api-listed-gateway-instance
- name: ListedGateway
  property_count: 3
  slug: mediaconnect-api-listed-gateway
- name: MaintenanceDay
  property_count: 0
  slug: mediaconnect-api-maintenance-day
- name: Maintenance
  property_count: 4
  slug: mediaconnect-api-maintenance
- name: MaxResults
  property_count: 0
  slug: mediaconnect-api-max-results
- name: MediaStreamAttributesRequest
  property_count: 2
  slug: mediaconnect-api-media-stream-attributes-request
- name: MediaStreamAttributes
  property_count: 2
  slug: mediaconnect-api-media-stream-attributes
- name: MediaStreamOutputConfigurationRequest
  property_count: 4
  slug: mediaconnect-api-media-stream-output-configuration-request
- name: MediaStreamOutputConfiguration
  property_count: 4
  slug: mediaconnect-api-media-stream-output-configuration
- name: MediaStream
  property_count: 8
  slug: mediaconnect-api-media-stream
- name: MediaStreamSourceConfigurationRequest
  property_count: 3
  slug: mediaconnect-api-media-stream-source-configuration-request
- name: MediaStreamSourceConfiguration
  property_count: 3
  slug: mediaconnect-api-media-stream-source-configuration
- name: MediaStreamType
  property_count: 0
  slug: mediaconnect-api-media-stream-type
- name: MessageDetail
  property_count: 3
  slug: mediaconnect-api-message-detail
- name: Messages
  property_count: 1
  slug: mediaconnect-api-messages
- name: NetworkInterfaceType
  property_count: 0
  slug: mediaconnect-api-network-interface-type
- name: Offering
  property_count: 8
  slug: mediaconnect-api-offering
- name: Output
  property_count: 15
  slug: mediaconnect-api-output
- name: PriceUnits
  property_count: 0
  slug: mediaconnect-api-price-units
- name: Protocol
  property_count: 0
  slug: mediaconnect-api-protocol
- name: PurchaseOfferingRequest
  property_count: 2
  slug: mediaconnect-api-purchase-offering-request
- name: PurchaseOfferingResponse
  property_count: 1
  slug: mediaconnect-api-purchase-offering-response
- name: Range
  property_count: 0
  slug: mediaconnect-api-range
- name: RemoveBridgeOutputRequest
  property_count: 0
  slug: mediaconnect-api-remove-bridge-output-request
- name: RemoveBridgeOutputResponse
  property_count: 2
  slug: mediaconnect-api-remove-bridge-output-response
- name: RemoveBridgeSourceRequest
  property_count: 0
  slug: mediaconnect-api-remove-bridge-source-request
- name: RemoveBridgeSourceResponse
  property_count: 2
  slug: mediaconnect-api-remove-bridge-source-response
- name: RemoveFlowMediaStreamRequest
  property_count: 0
  slug: mediaconnect-api-remove-flow-media-stream-request
- name: RemoveFlowMediaStreamResponse
  property_count: 2
  slug: mediaconnect-api-remove-flow-media-stream-response
- name: RemoveFlowOutputRequest
  property_count: 0
  slug: mediaconnect-api-remove-flow-output-request
- name: RemoveFlowOutputResponse
  property_count: 2
  slug: mediaconnect-api-remove-flow-output-response
- name: RemoveFlowSourceRequest
  property_count: 0
  slug: mediaconnect-api-remove-flow-source-request
- name: RemoveFlowSourceResponse
  property_count: 2
  slug: mediaconnect-api-remove-flow-source-response
- name: RemoveFlowVpcInterfaceRequest
  property_count: 0
  slug: mediaconnect-api-remove-flow-vpc-interface-request
- name: RemoveFlowVpcInterfaceResponse
  property_count: 3
  slug: mediaconnect-api-remove-flow-vpc-interface-response
- name: Reservation
  property_count: 13
  slug: mediaconnect-api-reservation
- name: ReservationState
  property_count: 0
  slug: mediaconnect-api-reservation-state
- name: ResourceSpecification
  property_count: 2
  slug: mediaconnect-api-resource-specification
- name: ResourceType
  property_count: 0
  slug: mediaconnect-api-resource-type
- name: RevokeFlowEntitlementRequest
  property_count: 0
  slug: mediaconnect-api-revoke-flow-entitlement-request
- name: RevokeFlowEntitlementResponse
  property_count: 2
  slug: mediaconnect-api-revoke-flow-entitlement-response
- name: ScanMode
  property_count: 0
  slug: mediaconnect-api-scan-mode
- name: SetGatewayBridgeSourceRequest
  property_count: 2
  slug: mediaconnect-api-set-gateway-bridge-source-request
- name: SetSourceRequest
  property_count: 19
  slug: mediaconnect-api-set-source-request
- name: SourcePriority
  property_count: 1
  slug: mediaconnect-api-source-priority
- name: Source
  property_count: 15
  slug: mediaconnect-api-source
- name: SourceType
  property_count: 0
  slug: mediaconnect-api-source-type
- name: StartFlowRequest
  property_count: 0
  slug: mediaconnect-api-start-flow-request
- name: StartFlowResponse
  property_count: 2
  slug: mediaconnect-api-start-flow-response
- name: State
  property_count: 0
  slug: mediaconnect-api-state
- name: Status
  property_count: 0
  slug: mediaconnect-api-status
- name: StopFlowRequest
  property_count: 0
  slug: mediaconnect-api-stop-flow-request
- name: StopFlowResponse
  property_count: 2
  slug: mediaconnect-api-stop-flow-response
- name: TagResourceRequest
  property_count: 1
  slug: mediaconnect-api-tag-resource-request
- name: Tcs
  property_count: 0
  slug: mediaconnect-api-tcs
- name: Transport
  property_count: 13
  slug: mediaconnect-api-transport
- name: UntagResourceRequest
  property_count: 0
  slug: mediaconnect-api-untag-resource-request
- name: UpdateBridgeFlowSourceRequest
  property_count: 2
  slug: mediaconnect-api-update-bridge-flow-source-request
- name: UpdateBridgeNetworkOutputRequest
  property_count: 5
  slug: mediaconnect-api-update-bridge-network-output-request
- name: UpdateBridgeNetworkSourceRequest
  property_count: 4
  slug: mediaconnect-api-update-bridge-network-source-request
- name: UpdateBridgeOutputRequest
  property_count: 1
  slug: mediaconnect-api-update-bridge-output-request
- name: UpdateBridgeOutputResponse
  property_count: 2
  slug: mediaconnect-api-update-bridge-output-response
- name: UpdateBridgeRequest
  property_count: 3
  slug: mediaconnect-api-update-bridge-request
- name: UpdateBridgeResponse
  property_count: 1
  slug: mediaconnect-api-update-bridge-response
- name: UpdateBridgeSourceRequest
  property_count: 2
  slug: mediaconnect-api-update-bridge-source-request
- name: UpdateBridgeSourceResponse
  property_count: 2
  slug: mediaconnect-api-update-bridge-source-response
- name: UpdateBridgeStateRequest
  property_count: 1
  slug: mediaconnect-api-update-bridge-state-request
- name: UpdateBridgeStateResponse
  property_count: 2
  slug: mediaconnect-api-update-bridge-state-response
- name: UpdateEgressGatewayBridgeRequest
  property_count: 1
  slug: mediaconnect-api-update-egress-gateway-bridge-request
- name: UpdateEncryption
  property_count: 9
  slug: mediaconnect-api-update-encryption
- name: UpdateFailoverConfig
  property_count: 4
  slug: mediaconnect-api-update-failover-config
- name: UpdateFlowEntitlementRequest
  property_count: 4
  slug: mediaconnect-api-update-flow-entitlement-request
- name: UpdateFlowEntitlementResponse
  property_count: 2
  slug: mediaconnect-api-update-flow-entitlement-response
- name: UpdateFlowMediaStreamRequest
  property_count: 5
  slug: mediaconnect-api-update-flow-media-stream-request
- name: UpdateFlowMediaStreamResponse
  property_count: 2
  slug: mediaconnect-api-update-flow-media-stream-response
- name: UpdateFlowOutputRequest
  property_count: 15
  slug: mediaconnect-api-update-flow-output-request
- name: UpdateFlowOutputResponse
  property_count: 2
  slug: mediaconnect-api-update-flow-output-response
- name: UpdateFlowRequest
  property_count: 2
  slug: mediaconnect-api-update-flow-request
- name: UpdateFlowResponse
  property_count: 1
  slug: mediaconnect-api-update-flow-response
- name: UpdateFlowSourceRequest
  property_count: 18
  slug: mediaconnect-api-update-flow-source-request
- name: UpdateFlowSourceResponse
  property_count: 2
  slug: mediaconnect-api-update-flow-source-response
- name: UpdateGatewayBridgeSourceRequest
  property_count: 2
  slug: mediaconnect-api-update-gateway-bridge-source-request
- name: UpdateGatewayInstanceRequest
  property_count: 1
  slug: mediaconnect-api-update-gateway-instance-request
- name: UpdateGatewayInstanceResponse
  property_count: 2
  slug: mediaconnect-api-update-gateway-instance-response
- name: UpdateIngressGatewayBridgeRequest
  property_count: 2
  slug: mediaconnect-api-update-ingress-gateway-bridge-request
- name: UpdateMaintenance
  property_count: 3
  slug: mediaconnect-api-update-maintenance
- name: VpcInterfaceAttachment
  property_count: 1
  slug: mediaconnect-api-vpc-interface-attachment
- name: VpcInterfaceRequest
  property_count: 5
  slug: mediaconnect-api-vpc-interface-request
- name: VpcInterface
  property_count: 6
  slug: mediaconnect-api-vpc-interface
json_structures:
- name: Mediaconnect Api __Boolean Structure
  property_count: 0
  slug: mediaconnect-api-__boolean-structure
- name: Mediaconnect Api __Double Structure
  property_count: 0
  slug: mediaconnect-api-__double-structure
- name: Mediaconnect Api __Integer Structure
  property_count: 0
  slug: mediaconnect-api-__integer-structure
- name: Mediaconnect Api __List Of Add Bridge Output Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-add-bridge-output-request-structure
- name: Mediaconnect Api __List Of Add Bridge Source Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-add-bridge-source-request-structure
- name: Mediaconnect Api __List Of Add Media Stream Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-add-media-stream-request-structure
- name: Mediaconnect Api __List Of Add Output Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-add-output-request-structure
- name: Mediaconnect Api __List Of Bridge Output Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-bridge-output-structure
- name: Mediaconnect Api __List Of Bridge Source Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-bridge-source-structure
- name: Mediaconnect Api __List Of Destination Configuration Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-destination-configuration-request-structure
- name: Mediaconnect Api __List Of Destination Configuration Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-destination-configuration-structure
- name: Mediaconnect Api __List Of Entitlement Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-entitlement-structure
- name: Mediaconnect Api __List Of Gateway Network Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-gateway-network-structure
- name: Mediaconnect Api __List Of Grant Entitlement Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-grant-entitlement-request-structure
- name: Mediaconnect Api __List Of Input Configuration Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-input-configuration-request-structure
- name: Mediaconnect Api __List Of Input Configuration Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-input-configuration-structure
- name: Mediaconnect Api __List Of Listed Bridge Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-bridge-structure
- name: Mediaconnect Api __List Of Listed Entitlement Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-entitlement-structure
- name: Mediaconnect Api __List Of Listed Flow Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-flow-structure
- name: Mediaconnect Api __List Of Listed Gateway Instance Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-gateway-instance-structure
- name: Mediaconnect Api __List Of Listed Gateway Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-listed-gateway-structure
- name: Mediaconnect Api __List Of Media Stream Output Configuration Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-output-configuration-request-structure
- name: Mediaconnect Api __List Of Media Stream Output Configuration Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-output-configuration-structure
- name: Mediaconnect Api __List Of Media Stream Source Configuration Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-source-configuration-request-structure
- name: Mediaconnect Api __List Of Media Stream Source Configuration Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-source-configuration-structure
- name: Mediaconnect Api __List Of Media Stream Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-media-stream-structure
- name: Mediaconnect Api __List Of Message Detail Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-message-detail-structure
- name: Mediaconnect Api __List Of Offering Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-offering-structure
- name: Mediaconnect Api __List Of Output Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-output-structure
- name: Mediaconnect Api __List Of Reservation Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-reservation-structure
- name: Mediaconnect Api __List Of Set Source Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-set-source-request-structure
- name: Mediaconnect Api __List Of Source Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-source-structure
- name: Mediaconnect Api __List Of Vpc Interface Request Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-vpc-interface-request-structure
- name: Mediaconnect Api __List Of Vpc Interface Structure
  property_count: 0
  slug: mediaconnect-api-__list-of-vpc-interface-structure
- name: Mediaconnect Api __List Of__Integer Structure
  property_count: 0
  slug: mediaconnect-api-__list-of__integer-structure
- name: Mediaconnect Api __List Of__String Structure
  property_count: 0
  slug: mediaconnect-api-__list-of__string-structure
- name: Mediaconnect Api __Map Of__String Structure
  property_count: 0
  slug: mediaconnect-api-__map-of__string-structure
- name: Mediaconnect Api __String Structure
  property_count: 0
  slug: mediaconnect-api-__string-structure
- name: Mediaconnect Api Add Bridge Flow Source Request Structure
  property_count: 3
  slug: mediaconnect-api-add-bridge-flow-source-request-structure
- name: Mediaconnect Api Add Bridge Network Output Request Structure
  property_count: 6
  slug: mediaconnect-api-add-bridge-network-output-request-structure
- name: Mediaconnect Api Add Bridge Network Source Request Structure
  property_count: 5
  slug: mediaconnect-api-add-bridge-network-source-request-structure
- name: Mediaconnect Api Add Bridge Output Request Structure
  property_count: 1
  slug: mediaconnect-api-add-bridge-output-request-structure
- name: Mediaconnect Api Add Bridge Outputs Request Structure
  property_count: 1
  slug: mediaconnect-api-add-bridge-outputs-request-structure
- name: Mediaconnect Api Add Bridge Outputs Response Structure
  property_count: 2
  slug: mediaconnect-api-add-bridge-outputs-response-structure
- name: Mediaconnect Api Add Bridge Source Request Structure
  property_count: 2
  slug: mediaconnect-api-add-bridge-source-request-structure
- name: Mediaconnect Api Add Bridge Sources Request Structure
  property_count: 1
  slug: mediaconnect-api-add-bridge-sources-request-structure
- name: Mediaconnect Api Add Bridge Sources Response Structure
  property_count: 2
  slug: mediaconnect-api-add-bridge-sources-response-structure
- name: Mediaconnect Api Add Egress Gateway Bridge Request Structure
  property_count: 1
  slug: mediaconnect-api-add-egress-gateway-bridge-request-structure
- name: Mediaconnect Api Add Flow Media Streams Request Structure
  property_count: 1
  slug: mediaconnect-api-add-flow-media-streams-request-structure
- name: Mediaconnect Api Add Flow Media Streams Response Structure
  property_count: 2
  slug: mediaconnect-api-add-flow-media-streams-response-structure
- name: Mediaconnect Api Add Flow Outputs Request Structure
  property_count: 1
  slug: mediaconnect-api-add-flow-outputs-request-structure
- name: Mediaconnect Api Add Flow Outputs Response Structure
  property_count: 2
  slug: mediaconnect-api-add-flow-outputs-response-structure
- name: Mediaconnect Api Add Flow Outputs420 Exception Structure
  property_count: 0
  slug: mediaconnect-api-add-flow-outputs420-exception-structure
- name: Mediaconnect Api Add Flow Sources Request Structure
  property_count: 1
  slug: mediaconnect-api-add-flow-sources-request-structure
- name: Mediaconnect Api Add Flow Sources Response Structure
  property_count: 2
  slug: mediaconnect-api-add-flow-sources-response-structure
- name: Mediaconnect Api Add Flow Vpc Interfaces Request Structure
  property_count: 1
  slug: mediaconnect-api-add-flow-vpc-interfaces-request-structure
- name: Mediaconnect Api Add Flow Vpc Interfaces Response Structure
  property_count: 2
  slug: mediaconnect-api-add-flow-vpc-interfaces-response-structure
- name: Mediaconnect Api Add Ingress Gateway Bridge Request Structure
  property_count: 2
  slug: mediaconnect-api-add-ingress-gateway-bridge-request-structure
- name: Mediaconnect Api Add Maintenance Structure
  property_count: 2
  slug: mediaconnect-api-add-maintenance-structure
- name: Mediaconnect Api Add Media Stream Request Structure
  property_count: 7
  slug: mediaconnect-api-add-media-stream-request-structure
- name: Mediaconnect Api Add Output Request Structure
  property_count: 15
  slug: mediaconnect-api-add-output-request-structure
- name: Mediaconnect Api Algorithm Structure
  property_count: 0
  slug: mediaconnect-api-algorithm-structure
- name: Mediaconnect Api Bridge Flow Output Structure
  property_count: 3
  slug: mediaconnect-api-bridge-flow-output-structure
- name: Mediaconnect Api Bridge Flow Source Structure
  property_count: 4
  slug: mediaconnect-api-bridge-flow-source-structure
- name: Mediaconnect Api Bridge Network Output Structure
  property_count: 6
  slug: mediaconnect-api-bridge-network-output-structure
- name: Mediaconnect Api Bridge Network Source Structure
  property_count: 5
  slug: mediaconnect-api-bridge-network-source-structure
- name: Mediaconnect Api Bridge Output Structure
  property_count: 2
  slug: mediaconnect-api-bridge-output-structure
- name: Mediaconnect Api Bridge Placement Structure
  property_count: 0
  slug: mediaconnect-api-bridge-placement-structure
- name: Mediaconnect Api Bridge Source Structure
  property_count: 2
  slug: mediaconnect-api-bridge-source-structure
- name: Mediaconnect Api Bridge State Structure
  property_count: 0
  slug: mediaconnect-api-bridge-state-structure
- name: Mediaconnect Api Bridge Structure
  property_count: 10
  slug: mediaconnect-api-bridge-structure
- name: Mediaconnect Api Colorimetry Structure
  property_count: 0
  slug: mediaconnect-api-colorimetry-structure
- name: Mediaconnect Api Connection Status Structure
  property_count: 0
  slug: mediaconnect-api-connection-status-structure
- name: Mediaconnect Api Create Bridge Request Structure
  property_count: 7
  slug: mediaconnect-api-create-bridge-request-structure
- name: Mediaconnect Api Create Bridge Response Structure
  property_count: 1
  slug: mediaconnect-api-create-bridge-response-structure
- name: Mediaconnect Api Create Bridge420 Exception Structure
  property_count: 0
  slug: mediaconnect-api-create-bridge420-exception-structure
- name: Mediaconnect Api Create Flow Request Structure
  property_count: 10
  slug: mediaconnect-api-create-flow-request-structure
- name: Mediaconnect Api Create Flow Response Structure
  property_count: 1
  slug: mediaconnect-api-create-flow-response-structure
- name: Mediaconnect Api Create Flow420 Exception Structure
  property_count: 0
  slug: mediaconnect-api-create-flow420-exception-structure
- name: Mediaconnect Api Create Gateway Request Structure
  property_count: 3
  slug: mediaconnect-api-create-gateway-request-structure
- name: Mediaconnect Api Create Gateway Response Structure
  property_count: 1
  slug: mediaconnect-api-create-gateway-response-structure
- name: Mediaconnect Api Create Gateway420 Exception Structure
  property_count: 0
  slug: mediaconnect-api-create-gateway420-exception-structure
- name: Mediaconnect Api Delete Bridge Request Structure
  property_count: 0
  slug: mediaconnect-api-delete-bridge-request-structure
- name: Mediaconnect Api Delete Bridge Response Structure
  property_count: 1
  slug: mediaconnect-api-delete-bridge-response-structure
- name: Mediaconnect Api Delete Flow Request Structure
  property_count: 0
  slug: mediaconnect-api-delete-flow-request-structure
- name: Mediaconnect Api Delete Flow Response Structure
  property_count: 2
  slug: mediaconnect-api-delete-flow-response-structure
- name: Mediaconnect Api Delete Gateway Request Structure
  property_count: 0
  slug: mediaconnect-api-delete-gateway-request-structure
- name: Mediaconnect Api Delete Gateway Response Structure
  property_count: 1
  slug: mediaconnect-api-delete-gateway-response-structure
- name: Mediaconnect Api Deregister Gateway Instance Request Structure
  property_count: 0
  slug: mediaconnect-api-deregister-gateway-instance-request-structure
- name: Mediaconnect Api Deregister Gateway Instance Response Structure
  property_count: 2
  slug: mediaconnect-api-deregister-gateway-instance-response-structure
- name: Mediaconnect Api Describe Bridge Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-bridge-request-structure
- name: Mediaconnect Api Describe Bridge Response Structure
  property_count: 1
  slug: mediaconnect-api-describe-bridge-response-structure
- name: Mediaconnect Api Describe Flow Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-flow-request-structure
- name: Mediaconnect Api Describe Flow Response Structure
  property_count: 2
  slug: mediaconnect-api-describe-flow-response-structure
- name: Mediaconnect Api Describe Gateway Instance Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-gateway-instance-request-structure
- name: Mediaconnect Api Describe Gateway Instance Response Structure
  property_count: 1
  slug: mediaconnect-api-describe-gateway-instance-response-structure
- name: Mediaconnect Api Describe Gateway Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-gateway-request-structure
- name: Mediaconnect Api Describe Gateway Response Structure
  property_count: 1
  slug: mediaconnect-api-describe-gateway-response-structure
- name: Mediaconnect Api Describe Offering Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-offering-request-structure
- name: Mediaconnect Api Describe Offering Response Structure
  property_count: 1
  slug: mediaconnect-api-describe-offering-response-structure
- name: Mediaconnect Api Describe Reservation Request Structure
  property_count: 0
  slug: mediaconnect-api-describe-reservation-request-structure
- name: Mediaconnect Api Describe Reservation Response Structure
  property_count: 1
  slug: mediaconnect-api-describe-reservation-response-structure
- name: Mediaconnect Api Desired State Structure
  property_count: 0
  slug: mediaconnect-api-desired-state-structure
- name: Mediaconnect Api Destination Configuration Request Structure
  property_count: 3
  slug: mediaconnect-api-destination-configuration-request-structure
- name: Mediaconnect Api Destination Configuration Structure
  property_count: 4
  slug: mediaconnect-api-destination-configuration-structure
- name: Mediaconnect Api Duration Units Structure
  property_count: 0
  slug: mediaconnect-api-duration-units-structure
- name: Mediaconnect Api Egress Gateway Bridge Structure
  property_count: 2
  slug: mediaconnect-api-egress-gateway-bridge-structure
- name: Mediaconnect Api Encoder Profile Structure
  property_count: 0
  slug: mediaconnect-api-encoder-profile-structure
- name: Mediaconnect Api Encoding Name Structure
  property_count: 0
  slug: mediaconnect-api-encoding-name-structure
- name: Mediaconnect Api Encoding Parameters Request Structure
  property_count: 2
  slug: mediaconnect-api-encoding-parameters-request-structure
- name: Mediaconnect Api Encoding Parameters Structure
  property_count: 2
  slug: mediaconnect-api-encoding-parameters-structure
- name: Mediaconnect Api Encryption Structure
  property_count: 9
  slug: mediaconnect-api-encryption-structure
- name: Mediaconnect Api Entitlement Status Structure
  property_count: 0
  slug: mediaconnect-api-entitlement-status-structure
- name: Mediaconnect Api Entitlement Structure
  property_count: 7
  slug: mediaconnect-api-entitlement-structure
- name: Mediaconnect Api Failover Config Structure
  property_count: 4
  slug: mediaconnect-api-failover-config-structure
- name: Mediaconnect Api Failover Mode Structure
  property_count: 0
  slug: mediaconnect-api-failover-mode-structure
- name: Mediaconnect Api Flow Structure
  property_count: 14
  slug: mediaconnect-api-flow-structure
- name: Mediaconnect Api Fmtp Request Structure
  property_count: 7
  slug: mediaconnect-api-fmtp-request-structure
- name: Mediaconnect Api Fmtp Structure
  property_count: 7
  slug: mediaconnect-api-fmtp-structure
- name: Mediaconnect Api Gateway Bridge Source Structure
  property_count: 2
  slug: mediaconnect-api-gateway-bridge-source-structure
- name: Mediaconnect Api Gateway Instance Structure
  property_count: 8
  slug: mediaconnect-api-gateway-instance-structure
- name: Mediaconnect Api Gateway Network Structure
  property_count: 2
  slug: mediaconnect-api-gateway-network-structure
- name: Mediaconnect Api Gateway State Structure
  property_count: 0
  slug: mediaconnect-api-gateway-state-structure
- name: Mediaconnect Api Gateway Structure
  property_count: 6
  slug: mediaconnect-api-gateway-structure
- name: Mediaconnect Api Grant Entitlement Request Structure
  property_count: 6
  slug: mediaconnect-api-grant-entitlement-request-structure
- name: Mediaconnect Api Grant Flow Entitlements Request Structure
  property_count: 1
  slug: mediaconnect-api-grant-flow-entitlements-request-structure
- name: Mediaconnect Api Grant Flow Entitlements Response Structure
  property_count: 2
  slug: mediaconnect-api-grant-flow-entitlements-response-structure
- name: Mediaconnect Api Grant Flow Entitlements420 Exception Structure
  property_count: 0
  slug: mediaconnect-api-grant-flow-entitlements420-exception-structure
- name: Mediaconnect Api Ingress Gateway Bridge Structure
  property_count: 3
  slug: mediaconnect-api-ingress-gateway-bridge-structure
- name: Mediaconnect Api Input Configuration Request Structure
  property_count: 2
  slug: mediaconnect-api-input-configuration-request-structure
- name: Mediaconnect Api Input Configuration Structure
  property_count: 3
  slug: mediaconnect-api-input-configuration-structure
- name: Mediaconnect Api Instance State Structure
  property_count: 0
  slug: mediaconnect-api-instance-state-structure
- name: Mediaconnect Api Interface Request Structure
  property_count: 1
  slug: mediaconnect-api-interface-request-structure
- name: Mediaconnect Api Interface Structure
  property_count: 1
  slug: mediaconnect-api-interface-structure
- name: Mediaconnect Api Key Type Structure
  property_count: 0
  slug: mediaconnect-api-key-type-structure
- name: Mediaconnect Api List Bridges Request Structure
  property_count: 0
  slug: mediaconnect-api-list-bridges-request-structure
- name: Mediaconnect Api List Bridges Response Structure
  property_count: 2
  slug: mediaconnect-api-list-bridges-response-structure
- name: Mediaconnect Api List Entitlements Request Structure
  property_count: 0
  slug: mediaconnect-api-list-entitlements-request-structure
- name: Mediaconnect Api List Entitlements Response Structure
  property_count: 2
  slug: mediaconnect-api-list-entitlements-response-structure
- name: Mediaconnect Api List Flows Request Structure
  property_count: 0
  slug: mediaconnect-api-list-flows-request-structure
- name: Mediaconnect Api List Flows Response Structure
  property_count: 2
  slug: mediaconnect-api-list-flows-response-structure
- name: Mediaconnect Api List Gateway Instances Request Structure
  property_count: 0
  slug: mediaconnect-api-list-gateway-instances-request-structure
- name: Mediaconnect Api List Gateway Instances Response Structure
  property_count: 2
  slug: mediaconnect-api-list-gateway-instances-response-structure
- name: Mediaconnect Api List Gateways Request Structure
  property_count: 0
  slug: mediaconnect-api-list-gateways-request-structure
- name: Mediaconnect Api List Gateways Response Structure
  property_count: 2
  slug: mediaconnect-api-list-gateways-response-structure
- name: Mediaconnect Api List Offerings Request Structure
  property_count: 0
  slug: mediaconnect-api-list-offerings-request-structure
- name: Mediaconnect Api List Offerings Response Structure
  property_count: 2
  slug: mediaconnect-api-list-offerings-response-structure
- name: Mediaconnect Api List Reservations Request Structure
  property_count: 0
  slug: mediaconnect-api-list-reservations-request-structure
- name: Mediaconnect Api List Reservations Response Structure
  property_count: 2
  slug: mediaconnect-api-list-reservations-response-structure
- name: Mediaconnect Api List Tags For Resource Request Structure
  property_count: 0
  slug: mediaconnect-api-list-tags-for-resource-request-structure
- name: Mediaconnect Api List Tags For Resource Response Structure
  property_count: 1
  slug: mediaconnect-api-list-tags-for-resource-response-structure
- name: Mediaconnect Api Listed Bridge Structure
  property_count: 5
  slug: mediaconnect-api-listed-bridge-structure
- name: Mediaconnect Api Listed Entitlement Structure
  property_count: 3
  slug: mediaconnect-api-listed-entitlement-structure
- name: Mediaconnect Api Listed Flow Structure
  property_count: 7
  slug: mediaconnect-api-listed-flow-structure
- name: Mediaconnect Api Listed Gateway Instance Structure
  property_count: 4
  slug: mediaconnect-api-listed-gateway-instance-structure
- name: Mediaconnect Api Listed Gateway Structure
  property_count: 3
  slug: mediaconnect-api-listed-gateway-structure
- name: Mediaconnect Api Maintenance Day Structure
  property_count: 0
  slug: mediaconnect-api-maintenance-day-structure
- name: Mediaconnect Api Maintenance Structure
  property_count: 4
  slug: mediaconnect-api-maintenance-structure
- name: Mediaconnect Api Max Results Structure
  property_count: 0
  slug: mediaconnect-api-max-results-structure
- name: Mediaconnect Api Media Stream Attributes Request Structure
  property_count: 2
  slug: mediaconnect-api-media-stream-attributes-request-structure
- name: Mediaconnect Api Media Stream Attributes Structure
  property_count: 2
  slug: mediaconnect-api-media-stream-attributes-structure
- name: Mediaconnect Api Media Stream Output Configuration Request Structure
  property_count: 4
  slug: mediaconnect-api-media-stream-output-configuration-request-structure
- name: Mediaconnect Api Media Stream Output Configuration Structure
  property_count: 4
  slug: mediaconnect-api-media-stream-output-configuration-structure
- name: Mediaconnect Api Media Stream Source Configuration Request Structure
  property_count: 3
  slug: mediaconnect-api-media-stream-source-configuration-request-structure
- name: Mediaconnect Api Media Stream Source Configuration Structure
  property_count: 3
  slug: mediaconnect-api-media-stream-source-configuration-structure
- name: Mediaconnect Api Media Stream Structure
  property_count: 8
  slug: mediaconnect-api-media-stream-structure
- name: Mediaconnect Api Media Stream Type Structure
  property_count: 0
  slug: mediaconnect-api-media-stream-type-structure
- name: Mediaconnect Api Message Detail Structure
  property_count: 3
  slug: mediaconnect-api-message-detail-structure
- name: Mediaconnect Api Messages Structure
  property_count: 1
  slug: mediaconnect-api-messages-structure
- name: Mediaconnect Api Network Interface Type Structure
  property_count: 0
  slug: mediaconnect-api-network-interface-type-structure
- name: Mediaconnect Api Offering Structure
  property_count: 8
  slug: mediaconnect-api-offering-structure
- name: Mediaconnect Api Output Structure
  property_count: 15
  slug: mediaconnect-api-output-structure
- name: Mediaconnect Api Price Units Structure
  property_count: 0
  slug: mediaconnect-api-price-units-structure
- name: Mediaconnect Api Protocol Structure
  property_count: 0
  slug: mediaconnect-api-protocol-structure
- name: Mediaconnect Api Purchase Offering Request Structure
  property_count: 2
  slug: mediaconnect-api-purchase-offering-request-structure
- name: Mediaconnect Api Purchase Offering Response Structure
  property_count: 1
  slug: mediaconnect-api-purchase-offering-response-structure
- name: Mediaconnect Api Range Structure
  property_count: 0
  slug: mediaconnect-api-range-structure
- name: Mediaconnect Api Remove Bridge Output Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-bridge-output-request-structure
- name: Mediaconnect Api Remove Bridge Output Response Structure
  property_count: 2
  slug: mediaconnect-api-remove-bridge-output-response-structure
- name: Mediaconnect Api Remove Bridge Source Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-bridge-source-request-structure
- name: Mediaconnect Api Remove Bridge Source Response Structure
  property_count: 2
  slug: mediaconnect-api-remove-bridge-source-response-structure
- name: Mediaconnect Api Remove Flow Media Stream Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-flow-media-stream-request-structure
- name: Mediaconnect Api Remove Flow Media Stream Response Structure
  property_count: 2
  slug: mediaconnect-api-remove-flow-media-stream-response-structure
- name: Mediaconnect Api Remove Flow Output Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-flow-output-request-structure
- name: Mediaconnect Api Remove Flow Output Response Structure
  property_count: 2
  slug: mediaconnect-api-remove-flow-output-response-structure
- name: Mediaconnect Api Remove Flow Source Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-flow-source-request-structure
- name: Mediaconnect Api Remove Flow Source Response Structure
  property_count: 2
  slug: mediaconnect-api-remove-flow-source-response-structure
- name: Mediaconnect Api Remove Flow Vpc Interface Request Structure
  property_count: 0
  slug: mediaconnect-api-remove-flow-vpc-interface-request-structure
- name: Mediaconnect Api Remove Flow Vpc Interface Response Structure
  property_count: 3
  slug: mediaconnect-api-remove-flow-vpc-interface-response-structure
- name: Mediaconnect Api Reservation State Structure
  property_count: 0
  slug: mediaconnect-api-reservation-state-structure
- name: Mediaconnect Api Reservation Structure
  property_count: 13
  slug: mediaconnect-api-reservation-structure
- name: Mediaconnect Api Resource Specification Structure
  property_count: 2
  slug: mediaconnect-api-resource-specification-structure
- name: Mediaconnect Api Resource Type Structure
  property_count: 0
  slug: mediaconnect-api-resource-type-structure
- name: Mediaconnect Api Revoke Flow Entitlement Request Structure
  property_count: 0
  slug: mediaconnect-api-revoke-flow-entitlement-request-structure
- name: Mediaconnect Api Revoke Flow Entitlement Response Structure
  property_count: 2
  slug: mediaconnect-api-revoke-flow-entitlement-response-structure
- name: Mediaconnect Api Scan Mode Structure
  property_count: 0
  slug: mediaconnect-api-scan-mode-structure
- name: Mediaconnect Api Set Gateway Bridge Source Request Structure
  property_count: 2
  slug: mediaconnect-api-set-gateway-bridge-source-request-structure
- name: Mediaconnect Api Set Source Request Structure
  property_count: 19
  slug: mediaconnect-api-set-source-request-structure
- name: Mediaconnect Api Source Priority Structure
  property_count: 1
  slug: mediaconnect-api-source-priority-structure
- name: Mediaconnect Api Source Structure
  property_count: 15
  slug: mediaconnect-api-source-structure
- name: Mediaconnect Api Source Type Structure
  property_count: 0
  slug: mediaconnect-api-source-type-structure
- name: Mediaconnect Api Start Flow Request Structure
  property_count: 0
  slug: mediaconnect-api-start-flow-request-structure
- name: Mediaconnect Api Start Flow Response Structure
  property_count: 2
  slug: mediaconnect-api-start-flow-response-structure
- name: Mediaconnect Api State Structure
  property_count: 0
  slug: mediaconnect-api-state-structure
- name: Mediaconnect Api Status Structure
  property_count: 0
  slug: mediaconnect-api-status-structure
- name: Mediaconnect Api Stop Flow Request Structure
  property_count: 0
  slug: mediaconnect-api-stop-flow-request-structure
- name: Mediaconnect Api Stop Flow Response Structure
  property_count: 2
  slug: mediaconnect-api-stop-flow-response-structure
- name: Mediaconnect Api Tag Resource Request Structure
  property_count: 1
  slug: mediaconnect-api-tag-resource-request-structure
- name: Mediaconnect Api Tcs Structure
  property_count: 0
  slug: mediaconnect-api-tcs-structure
- name: Mediaconnect Api Transport Structure
  property_count: 13
  slug: mediaconnect-api-transport-structure
- name: Mediaconnect Api Untag Resource Request Structure
  property_count: 0
  slug: mediaconnect-api-untag-resource-request-structure
- name: Mediaconnect Api Update Bridge Flow Source Request Structure
  property_count: 2
  slug: mediaconnect-api-update-bridge-flow-source-request-structure
- name: Mediaconnect Api Update Bridge Network Output Request Structure
  property_count: 5
  slug: mediaconnect-api-update-bridge-network-output-request-structure
- name: Mediaconnect Api Update Bridge Network Source Request Structure
  property_count: 4
  slug: mediaconnect-api-update-bridge-network-source-request-structure
- name: Mediaconnect Api Update Bridge Output Request Structure
  property_count: 1
  slug: mediaconnect-api-update-bridge-output-request-structure
- name: Mediaconnect Api Update Bridge Output Response Structure
  property_count: 2
  slug: mediaconnect-api-update-bridge-output-response-structure
- name: Mediaconnect Api Update Bridge Request Structure
  property_count: 3
  slug: mediaconnect-api-update-bridge-request-structure
- name: Mediaconnect Api Update Bridge Response Structure
  property_count: 1
  slug: mediaconnect-api-update-bridge-response-structure
- name: Mediaconnect Api Update Bridge Source Request Structure
  property_count: 2
  slug: mediaconnect-api-update-bridge-source-request-structure
- name: Mediaconnect Api Update Bridge Source Response Structure
  property_count: 2
  slug: mediaconnect-api-update-bridge-source-response-structure
- name: Mediaconnect Api Update Bridge State Request Structure
  property_count: 1
  slug: mediaconnect-api-update-bridge-state-request-structure
- name: Mediaconnect Api Update Bridge State Response Structure
  property_count: 2
  slug: mediaconnect-api-update-bridge-state-response-structure
- name: Mediaconnect Api Update Egress Gateway Bridge Request Structure
  property_count: 1
  slug: mediaconnect-api-update-egress-gateway-bridge-request-structure
- name: Mediaconnect Api Update Encryption Structure
  property_count: 9
  slug: mediaconnect-api-update-encryption-structure
- name: Mediaconnect Api Update Failover Config Structure
  property_count: 4
  slug: mediaconnect-api-update-failover-config-structure
- name: Mediaconnect Api Update Flow Entitlement Request Structure
  property_count: 4
  slug: mediaconnect-api-update-flow-entitlement-request-structure
- name: Mediaconnect Api Update Flow Entitlement Response Structure
  property_count: 2
  slug: mediaconnect-api-update-flow-entitlement-response-structure
- name: Mediaconnect Api Update Flow Media Stream Request Structure
  property_count: 5
  slug: mediaconnect-api-update-flow-media-stream-request-structure
- name: Mediaconnect Api Update Flow Media Stream Response Structure
  property_count: 2
  slug: mediaconnect-api-update-flow-media-stream-response-structure
- name: Mediaconnect Api Update Flow Output Request Structure
  property_count: 15
  slug: mediaconnect-api-update-flow-output-request-structure
- name: Mediaconnect Api Update Flow Output Response Structure
  property_count: 2
  slug: mediaconnect-api-update-flow-output-response-structure
- name: Mediaconnect Api Update Flow Request Structure
  property_count: 2
  slug: mediaconnect-api-update-flow-request-structure
- name: Mediaconnect Api Update Flow Response Structure
  property_count: 1
  slug: mediaconnect-api-update-flow-response-structure
- name: Mediaconnect Api Update Flow Source Request Structure
  property_count: 18
  slug: mediaconnect-api-update-flow-source-request-structure
- name: Mediaconnect Api Update Flow Source Response Structure
  property_count: 2
  slug: mediaconnect-api-update-flow-source-response-structure
- name: Mediaconnect Api Update Gateway Bridge Source Request Structure
  property_count: 2
  slug: mediaconnect-api-update-gateway-bridge-source-request-structure
- name: Mediaconnect Api Update Gateway Instance Request Structure
  property_count: 1
  slug: mediaconnect-api-update-gateway-instance-request-structure
- name: Mediaconnect Api Update Gateway Instance Response Structure
  property_count: 2
  slug: mediaconnect-api-update-gateway-instance-response-structure
- name: Mediaconnect Api Update Ingress Gateway Bridge Request Structure
  property_count: 2
  slug: mediaconnect-api-update-ingress-gateway-bridge-request-structure
- name: Mediaconnect Api Update Maintenance Structure
  property_count: 3
  slug: mediaconnect-api-update-maintenance-structure
- name: Mediaconnect Api Vpc Interface Attachment Structure
  property_count: 1
  slug: mediaconnect-api-vpc-interface-attachment-structure
- name: Mediaconnect Api Vpc Interface Request Structure
  property_count: 5
  slug: mediaconnect-api-vpc-interface-request-structure
- name: Mediaconnect Api Vpc Interface Structure
  property_count: 6
  slug: mediaconnect-api-vpc-interface-structure
jsonld:
- class_count: 246
  name: Amazon Mediaconnect Api Context
  property_count: 170
  slug: amazon-mediaconnect-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MediaConnect
nav: Providers
network: true
overview: 'Amazon MediaConnect publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bridges API, Entitlements API, Flows API, and 5 more. Tagged areas include Broadcasting, Live Video, Media, and Media Transport.


  The Amazon MediaConnect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MediaConnect''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Mediaconnect Plans Pricing
  plan_count: 3
  slug: amazon-mediaconnect-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Amazon Mediaconnect Rate Limits
  slug: amazon-mediaconnect-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon MediaConnect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-mediaconnect-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Amazon MediaConnect API Rules
  rule_count: 27
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 15
  slug: amazon-mediaconnect-spectral-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 68.7
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconnect/refs/heads/main/screenshots/amazon-mediaconnect-2026-06-20T171739.png
security:
- kind: authentication
  name: Amazon Mediaconnect Authentication
  slug: amazon-mediaconnect-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Mediaconnect Domain Security
  slug: amazon-mediaconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Mediaconnect Vulnerability Disclosure
  slug: amazon-mediaconnect-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Mediaconnect Trust Center
  slug: amazon-mediaconnect-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-mediaconnect
tags:
- Broadcasting
- Live Video
- Media
- Media Transport
use_cases:
- description: Transport continuous broadcast streams reliably for round-the-clock television channels.
  name: 24/7 TV Channel Operation
- description: Manage event-based video distribution for sports, concerts, news, and other live events.
  name: Live Event Streaming
- description: Share live video feeds with partners and customers through controlled entitlements.
  name: Content Sharing
- description: Provide redundant video pathways for business continuity in broadcast workflows.
  name: Disaster Recovery
website: https://aws.amazon.com/mediaconnect/
---
