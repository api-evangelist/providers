---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Gravatar Agentic Access
  operation_count: 12
  slug: gravatar-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 4
apis:
- description: Operations about user avatars
  name: Gravatar avatars API
  slug: gravatar-avatars-api
- description: Experimental operations that might be subject to change. Use with caution.
  name: Gravatar experimental API
  slug: gravatar-experimental-api
- description: Operations about user profiles
  name: Gravatar profiles API
  slug: gravatar-profiles-api
- description: Operations about QR codes
  name: Gravatar qr-code API
  slug: gravatar-qr-code-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gravatar Public avatars API
  slug: open-gravatar-avatars-api
- collection_type: open
  name: Gravatar Public avatars experimental API
  slug: open-gravatar-experimental-api
- collection_type: open
  name: Gravatar Public avatars profiles API
  slug: open-gravatar-profiles-api
- collection_type: open
  name: Gravatar Public avatars qr-code API
  slug: open-gravatar-qr-code-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gravatar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gravatar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gravatar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gravatar-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.gravatar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gravatar.com/api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.gravatar.com/v3/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gravatar.com/rest/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.gravatar.com/rest/getting-started/#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.gravatar.com/general/pricing/
- group: operate
  title: ''
  type: Status
  url: http://status.automattic.com/9931/136545/Gravatar
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Automattic/gravatar
- group: build
  title: ''
  type: AndroidSDK
  url: https://docs.gravatar.com/sdk/android/
- group: build
  title: ''
  type: iOSSDK
  url: https://docs.gravatar.com/sdk/ios/
- group: other
  title: ''
  type: APIExplorer
  url: https://docs.gravatar.com/api/explorer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gravatar.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gravatar.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.gravatar.com/feed/
created: '2026-06-13'
description: Gravatar (Globally Recognized Avatar) is a service that provides universally recognized avatars and rich identity profiles tied to email addresses via SHA256 hash. Developers can fetch user avatars, profile information, verified social accounts, and identity data using a REST API with API key or OAuth authentication. The service offers both a public avatar CDN (no auth required) and a REST API (v3) for profiles, avatar management, QR codes, and verified account lookups.
examples:
- key_count: 7
  name: Associatedemail
  slug: associatedEmail
- key_count: 7
  name: Deleteavatar
  slug: deleteAvatar
- key_count: 7
  name: Getavatars
  slug: getAvatars
- key_count: 8
  name: Getprofile
  slug: getProfile
- key_count: 7
  name: Getprofilebyid
  slug: getProfileById
- key_count: 7
  name: Getqrcodebysha256Hash
  slug: getQrCodeBySha256Hash
- key_count: 7
  name: Getverifiedaccountservices
  slug: getVerifiedAccountServices
- key_count: 7
  name: Searchprofilesbyverifiedaccount
  slug: searchProfilesByVerifiedAccount
- key_count: 7
  name: Setemailavatar
  slug: setEmailAvatar
- key_count: 7
  name: Updateavatar
  slug: updateAvatar
- key_count: 8
  name: Updateprofile
  slug: updateProfile
- key_count: 8
  name: Uploadavatar
  slug: uploadAvatar
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Gravatar does not expose a native GraphQL endpoint. This schema is a conceptual GraphQL representation of the Gravatar REST API v3, derived from the public REST types documented at https://docs.gravat
  name: Gravatar GraphQL
  slug: gravatar-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gravatar.png
json_schemas:
- name: AssociatedResponse
  property_count: 1
  slug: associatedresponse
- name: Avatar
  property_count: 6
  slug: avatar
- name: CryptoWalletAddress
  property_count: 2
  slug: cryptowalletaddress
- name: Error
  property_count: 2
  slug: error
- name: GalleryImage
  property_count: 2
  slug: galleryimage
- name: Interest
  property_count: 3
  slug: interest
- name: Language
  property_count: 4
  slug: language
- name: Link
  property_count: 2
  slug: link
- name: Profile
  property_count: 31
  slug: profile
- name: Rating
  property_count: 0
  slug: rating
- name: VerifiedAccount
  property_count: 5
  slug: verifiedaccount
jsonld:
- class_count: 0
  name: context Context
  property_count: 40
  slug: context
layout: provider
modified: '2026-06-13'
name: Gravatar
nav: Providers
network: true
overview: 'Gravatar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including avatars API, experimental API, profiles API, and 1 more. Tagged areas include Avatars, Identity, Profiles, Social, and Image.


  The Gravatar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gravatar''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, status page, engineering blog, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 16
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Gravatar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gravatar-jsonschema-spectral-rules
scopes:
- name: Gravatar Scopes
  scope_count: 3
  slug: gravatar-scopes
  summary_line: 3 scopes · implicit
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 63.5
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gravatar/refs/heads/main/screenshots/gravatar-2026-08-17T083454.png
security:
- kind: authentication
  name: Gravatar Authentication
  slug: gravatar-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gravatar Domain Security
  slug: gravatar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gravatar
tags:
- Avatars
- Identity
- Profiles
- Social
- Image
- GraphQL
- REST
website: https://docs.gravatar.com/
---
