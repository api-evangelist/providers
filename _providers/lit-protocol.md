---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
- acting_count: 22
  human_in_the_loop: 0
  name: Lit Protocol Agentic Access
  operation_count: 37
  slug: lit-protocol-agentic-access
  summary_line: 37 operations · 22 acting
api_count: 1
apis:
- description: 'Threshold-cryptography network of Lit nodes accessed via the Lit JS SDK for signing, encryption, decryption, and Lit Action execution. Direct REST access is via the Chipotle API; raw node JSON-RPC is '
  name: Lit Network Node JSON-RPC (SDK-mediated)
  slug: network-rpc
- description: The Account Management API from Lit Protocol — 28 operation(s) for account management.
  name: Lit Protocol Account Management API
  slug: lit-protocol-account-management-api
- description: The Actions API from Lit Protocol — 1 operation(s) for actions.
  name: Lit Protocol Actions API
  slug: lit-protocol-actions-api
- description: The Billing API from Lit Protocol — 4 operation(s) for billing.
  name: Lit Protocol Billing API
  slug: lit-protocol-billing-api
- description: The Configuration API from Lit Protocol — 4 operation(s) for configuration.
  name: Lit Protocol Configuration API
  slug: lit-protocol-configuration-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: lit-api-server Account Management API
  slug: open-lit-protocol-account-management-api
- collection_type: open
  name: lit-api-server Account Management Actions API
  slug: open-lit-protocol-actions-api
- collection_type: open
  name: lit-api-server Account Management Billing API
  slug: open-lit-protocol-billing-api
- collection_type: open
  name: lit-api-server Account Management Configuration API
  slug: open-lit-protocol-configuration-api
- collection_type: open
  name: lit-api-server
  slug: open-lit-protocol-core-v1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lit-protocol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lit-protocol-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LIT-Protocol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lit-protocol
- group: company
  title: ''
  type: Website
  url: https://www.litprotocol.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/lit-protocol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lit-protocol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lit-protocol-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.litprotocol.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://spark.litprotocol.com/rss/
created: '2026-05-08'
description: Lit Protocol is a decentralized key management network providing Programmable Key Pairs (PKPs), Lit Actions (off-chain JS execution), threshold encryption, and access-control conditions. The Chipotle Express API exposes account, PKP, and Lit Action management as REST endpoints alongside the JavaScript SDK.
finops:
- name: Lit Protocol Finops
  service_category: Web3
  slug: lit-protocol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lit-protocol.png
json_schemas:
- name: AccountOpResponse
  property_count: 1
  slug: lit-protocol-accountopresponse
- name: AddActionRequest
  property_count: 3
  slug: lit-protocol-addactionrequest
- name: AddActionToGroupRequest
  property_count: 2
  slug: lit-protocol-addactiontogrouprequest
- name: AddGroupRequest
  property_count: 4
  slug: lit-protocol-addgrouprequest
- name: AddGroupResponse
  property_count: 2
  slug: lit-protocol-addgroupresponse
- name: AddPkpToGroupRequest
  property_count: 2
  slug: lit-protocol-addpkptogrouprequest
- name: AddUsageApiKeyRequest
  property_count: 9
  slug: lit-protocol-addusageapikeyrequest
- name: AddUsageApiKeyResponse
  property_count: 2
  slug: lit-protocol-addusageapikeyresponse
- name: AddUsageApiKeyWithSignatureRequest
  property_count: 2
  slug: lit-protocol-addusageapikeywithsignaturerequest
- name: AddUsageApiKeyWithSignatureResponse
  property_count: 3
  slug: lit-protocol-addusageapikeywithsignatureresponse
- name: ApiKeyItem
  property_count: 13
  slug: lit-protocol-apikeyitem
- name: BillingBalanceResponse
  property_count: 2
  slug: lit-protocol-billingbalanceresponse
- name: ChainConfigKeysResponse
  property_count: 1
  slug: lit-protocol-chainconfigkeysresponse
- name: ConfirmPaymentRequest
  property_count: 1
  slug: lit-protocol-confirmpaymentrequest
- name: ConvertToChainSecuredAccountRequest
  property_count: 3
  slug: lit-protocol-converttochainsecuredaccountrequest
- name: CreatePaymentIntentRequest
  property_count: 1
  slug: lit-protocol-createpaymentintentrequest
- name: CreatePaymentIntentResponse
  property_count: 2
  slug: lit-protocol-createpaymentintentresponse
- name: CreateWalletResponse
  property_count: 1
  slug: lit-protocol-createwalletresponse
- name: CreateWalletWithSignatureRequest
  property_count: 2
  slug: lit-protocol-createwalletwithsignaturerequest
- name: CreateWalletWithSignatureResponse
  property_count: 2
  slug: lit-protocol-createwalletwithsignatureresponse
- name: DeleteActionRequest
  property_count: 1
  slug: lit-protocol-deleteactionrequest
- name: ErrMessage
  property_count: 0
  slug: lit-protocol-errmessage
- name: ListMetadataItem
  property_count: 3
  slug: lit-protocol-listmetadataitem
- name: LitActionClientConfigResponse
  property_count: 10
  slug: lit-protocol-litactionclientconfigresponse
- name: LitActionRequest
  property_count: 3
  slug: lit-protocol-litactionrequest
- name: LitActionResponse
  property_count: 3
  slug: lit-protocol-litactionresponse
- name: NewAccountRequest
  property_count: 3
  slug: lit-protocol-newaccountrequest
- name: NewAccountResponse
  property_count: 2
  slug: lit-protocol-newaccountresponse
- name: NodeChainConfigResponse
  property_count: 6
  slug: lit-protocol-nodechainconfigresponse
- name: RemoveActionFromGroupRequest
  property_count: 2
  slug: lit-protocol-removeactionfromgrouprequest
- name: RemoveGroupRequest
  property_count: 1
  slug: lit-protocol-removegrouprequest
- name: RemovePkpFromGroupRequest
  property_count: 2
  slug: lit-protocol-removepkpfromgrouprequest
- name: RemoveUsageApiKeyRequest
  property_count: 1
  slug: lit-protocol-removeusageapikeyrequest
- name: StripeConfigResponse
  property_count: 1
  slug: lit-protocol-stripeconfigresponse
- name: UpdateActionMetadataRequest
  property_count: 3
  slug: lit-protocol-updateactionmetadatarequest
- name: UpdateGroupRequest
  property_count: 5
  slug: lit-protocol-updategrouprequest
- name: UpdateUsageApiKeyMetadataRequest
  property_count: 3
  slug: lit-protocol-updateusageapikeymetadatarequest
- name: UpdateUsageApiKeyRequest
  property_count: 10
  slug: lit-protocol-updateusageapikeyrequest
- name: VersionResponse
  property_count: 4
  slug: lit-protocol-versionresponse
- name: WalletItem
  property_count: 4
  slug: lit-protocol-walletitem
json_structures:
- name: Lit Protocol Structure
  property_count: 0
  slug: lit-protocol-structure
layout: provider
modified: '2026-05-08'
name: Lit Protocol
nav: Providers
network: true
overview: 'Lit Protocol publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Actions API, Billing API, and 1 more. Tagged areas include Web3, Key Management, MPC, Programmable Keys, and Lit Actions.


  The Lit Protocol catalog on APIs.io includes 1 Spectral governance ruleset.


  Lit Protocol''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Lit Protocol Plans Pricing
  plan_count: 2
  slug: lit-protocol-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Lit Protocol Rate Limits
  slug: lit-protocol-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lit Protocol API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lit-protocol-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 67.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 32.7
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lit-protocol/refs/heads/main/screenshots/lit-protocol-2026-06-20T184559.png
security:
- kind: domain-security
  name: Lit Protocol Domain Security
  slug: lit-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lit-protocol
tags:
- Web3
- Key Management
- MPC
- Programmable Keys
- Lit Actions
website: https://www.litprotocol.com/
---
