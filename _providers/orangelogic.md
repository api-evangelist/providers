---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Orangelogic Agentic Access
  operation_count: 44
  slug: orangelogic-agentic-access
  summary_line: 44 operations · 22 acting
api_count: 33
apis:
- description: Authenticate against an Orange Logic instance and obtain tokens for subsequent calls. Supports OAuth 2.0 (client ID and secret), non-expiring bearer tokens, and basic username/password login. The OAut
  name: Orange Logic Authentication API
  slug: orangelogic-authentication-api
- baseURL: https://{OrangeLogicURL}/API
  baseurl_source: declared
  description: Find assets across the DAM with query criteria, field selection, pagination, sorting, and AI-powered semantic search. The confirmed endpoint is GET or POST /API/search/v4.0/search, accepting query, fi
  name: Orange Logic Search API
  slug: orangelogic-search-api
- description: Upload, import, retrieve, and manage digital assets and their representations - single-file uploads, batch uploads, cloud-storage imports, and large-file (>1.5GB) handling, plus content delivery via p
  name: Orange Logic Assets and Media API
  slug: orangelogic-assets-media-api
- description: Work directly with database objects - assets (images, video, audio), folders, groups, users, tags, keywords, and relationships - through generic CREATE, READ, UPDATE, and DELETE calls. Paths follow th
  name: Orange Logic DataTable API
  slug: orangelogic-datatable-api
- description: List and modify asset metadata - retrieve all metadata fields, update tags and linked fields, and manage language-specific field values. Includes batch edit and batch upsert operations. Endpoint ident
  name: Orange Logic Metadata API
  slug: orangelogic-metadata-api
- description: 'Manage user and contact accounts, group assignments, permissions, and organizational hierarchies. Handled through the DataTable object model (Users, Groups, Contacts). Exact endpoint identifiers vary '
  name: Orange Logic Users and Contacts API
  slug: orangelogic-users-contacts-api
- description: 'Subscribe to asset lifecycle events and send webhooks to a third-party service when assets are created, edited, or deleted. This is a server-to-endpoint HTTP callback surface, not a persistent socket '
  name: Orange Logic Webhooks API
  slug: orangelogic-webhooks-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Batcheditfields 4FQ V1 API from Orange Logic — 1 operation(s) for batcheditfields 4fq v1.
  name: Orange Logic Batcheditfields 4FQ V1 API
  slug: orangelogic-batcheditfields-4fq-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Batchupsert 4FY V1 API from Orange Logic — 1 operation(s) for batchupsert 4fy v1.
  name: Orange Logic Batchupsert 4FY V1 API
  slug: orangelogic-batchupsert-4fy-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Batchupsert Csv 4G3 V1 API from Orange Logic — 1 operation(s) for batchupsert csv 4g3 v1.
  name: Orange Logic Batchupsert Csv 4G3 V1 API
  slug: orangelogic-batchupsert-csv-4g3-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Batchupsertassetlinkswithcustomroute 41FD V2 API from Orange Logic — 1 operation(s) for batchupsertassetlinkswithcustomroute 41fd v2.
  name: Orange Logic Batchupsertassetlinkswithcustomroute 41FD V2 API
  slug: orangelogic-batchupsertassetlinkswithcustomroute-41fd-v2-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Bearerauthentication API from Orange Logic — 2 operation(s) for bearerauthentication.
  name: Orange Logic Bearerauthentication API
  slug: orangelogic-bearerauthentication-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Clientcredentialsauthentication API from Orange Logic — 1 operation(s) for clientcredentialsauthentication.
  name: Orange Logic Clientcredentialsauthentication API
  slug: orangelogic-clientcredentialsauthentication-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Complete 27 V1 API from Orange Logic — 1 operation(s) for complete 27 v1.
  name: Orange Logic Complete 27 V1 API
  slug: orangelogic-complete-27-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Create 22E V1 API from Orange Logic — 1 operation(s) for create 22e v1.
  name: Orange Logic Create 22E V1 API
  slug: orangelogic-create-22e-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The CreateCropLink API from Orange Logic — 1 operation(s) for createcroplink.
  name: Orange Logic Create Crop Link API
  slug: orangelogic-createcroplink-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Createsharelink 41M9 V1 API from Orange Logic — 1 operation(s) for createsharelink 41m9 v1.
  name: Orange Logic Createsharelink 41M9 V1 API
  slug: orangelogic-createsharelink-41m9-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Documents.All:ListFields API from Orange Logic — 1 operation(s) for documents.all:listfields.
  name: Orange Logic Documents.All:List Fields API
  slug: orangelogic-documents-all-listfields-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Documents.{Asset Type}.{Asset Subtype}:AssignLeadDocument API from Orange Logic — 1 operation(s) for documents.{asset type}.{asset subtype}:assignleaddocument.
  name: Orange Logic Documents.{Asset Type}.{Asset Subtype}:AssignLeadDocument API
  slug: orangelogic-documents-asset-type-asset-subtype-assignleaddocument-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getfilterinfo 4104 V1 API from Orange Logic — 1 operation(s) for getfilterinfo 4104 v1.
  name: Orange Logic Getfilterinfo 4104 V1 API
  slug: orangelogic-getfilterinfo-4104-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getlink 4HZ V1 API from Orange Logic — 1 operation(s) for getlink 4hz v1.
  name: Orange Logic Getlink 4HZ V1 API
  slug: orangelogic-getlink-4hz-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getlinks 45W V1 API from Orange Logic — 1 operation(s) for getlinks 45w v1.
  name: Orange Logic Getlinks 45W V1 API
  slug: orangelogic-getlinks-45w-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getpresignedlink 4ar V1 API from Orange Logic — 1 operation(s) for getpresignedlink 4ar v1.
  name: Orange Logic Getpresignedlink 4ar V1 API
  slug: orangelogic-getpresignedlink-4ar-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getpresignedlinks In Batch 4G8 V1 API from Orange Logic — 1 operation(s) for getpresignedlinks in batch 4g8 v1.
  name: Orange Logic Getpresignedlinks In Batch 4G8 V1 API
  slug: orangelogic-getpresignedlinks-in-batch-4g8-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getreport 4103 V1 API from Orange Logic — 1 operation(s) for getreport 4103 v1.
  name: Orange Logic Getreport 4103 V1 API
  slug: orangelogic-getreport-4103-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getreportinfo 4102 V1 API from Orange Logic — 1 operation(s) for getreportinfo 4102 v1.
  name: Orange Logic Getreportinfo 4102 V1 API
  slug: orangelogic-getreportinfo-4102-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getsharelinkstatus 41MA V1 API from Orange Logic — 1 operation(s) for getsharelinkstatus 41ma v1.
  name: Orange Logic Getsharelinkstatus 41MA V1 API
  slug: orangelogic-getsharelinkstatus-41ma-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Getwatermarkpresets 41MB V1 API from Orange Logic — 1 operation(s) for getwatermarkpresets 41mb v1.
  name: Orange Logic Getwatermarkpresets 41MB V1 API
  slug: orangelogic-getwatermarkpresets-41mb-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The InvalidateCloudfrontCache 2cl V1 API from Orange Logic — 1 operation(s) for invalidatecloudfrontcache 2cl v1.
  name: Orange Logic InvalidateCloudfrontCache 2cl V1 API
  slug: orangelogic-invalidatecloudfrontcache-2cl-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Item API from Orange Logic — 1 operation(s) for item.
  name: Orange Logic Item API
  slug: orangelogic-item-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The List All Database Objects API from Orange Logic — 1 operation(s) for list all database objects.
  name: Orange Logic List All Database Objects API
  slug: orangelogic-list-all-database-objects-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The ListCriteria API from Orange Logic — 1 operation(s) for listcriteria.
  name: Orange Logic List Criteria API
  slug: orangelogic-listcriteria-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The ListFields API from Orange Logic — 1 operation(s) for listfields.
  name: Orange Logic List Fields API
  slug: orangelogic-listfields-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Login API from Orange Logic — 1 operation(s) for login.
  name: Orange Logic Login API
  slug: orangelogic-login-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Oauth2 API from Orange Logic — 3 operation(s) for oauth2.
  name: Orange Logic Oauth2 API
  slug: orangelogic-oauth2-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Query Batchupsert 4G2 V1 API from Orange Logic — 1 operation(s) for query batchupsert 4g2 v1.
  name: Orange Logic Query Batchupsert 4G2 V1 API
  slug: orangelogic-query-batchupsert-4g2-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Querybatchupsertassetlinkswithcustomroutejobstatus 41FE V1 API from Orange Logic — 1 operation(s) for querybatchupsertassetlinkswithcustomroutejobstatus 41fe v1.
  name: Orange Logic Querybatchupsertassetlinkswithcustomroutejobstatus 41FE V1 API
  slug: orangelogic-querybatchupsertassetlinkswithcustomroutejobstatus-41fe-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The RegenerateProxiesForAsset API from Orange Logic — 1 operation(s) for regenerateproxiesforasset.
  name: Orange Logic Regenerate Proxies For Asset API
  slug: orangelogic-regenerateproxiesforasset-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Register 25 V1 API from Orange Logic — 1 operation(s) for register 25 v1.
  name: Orange Logic Register 25 V1 API
  slug: orangelogic-register-25-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Rotatesecret 22P V1 API from Orange Logic — 1 operation(s) for rotatesecret 22p v1.
  name: Orange Logic Rotatesecret 22P V1 API
  slug: orangelogic-rotatesecret-22p-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Search API from Orange Logic — 1 operation(s) for search.
  name: Orange Logic Search API
  slug: orangelogic-search-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Transaction API from Orange Logic — 1 operation(s) for transaction.
  name: Orange Logic Transaction API
  slug: orangelogic-transaction-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The UploadFileFromCloudStorage 4OY V1 API from Orange Logic — 1 operation(s) for uploadfilefromcloudstorage 4oy v1.
  name: Orange Logic UploadFileFromCloudStorage 4OY V1 API
  slug: orangelogic-uploadfilefromcloudstorage-4oy-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Uploadimageandgetlargestdownloadlink 4CM V1 API from Orange Logic — 1 operation(s) for uploadimageandgetlargestdownloadlink 4cm v1.
  name: Orange Logic Uploadimageandgetlargestdownloadlink 4CM V1 API
  slug: orangelogic-uploadimageandgetlargestdownloadlink-4cm-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Uploadmedia 4az V1 API from Orange Logic — 1 operation(s) for uploadmedia 4az v1.
  name: Orange Logic Uploadmedia 4az V1 API
  slug: orangelogic-uploadmedia-4az-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The Uploadmediawithurl 45L V1 API from Orange Logic — 1 operation(s) for uploadmediawithurl 45l v1.
  name: Orange Logic Uploadmediawithurl 45L V1 API
  slug: orangelogic-uploadmediawithurl-45l-v1-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The UploadNewMedia API from Orange Logic — 1 operation(s) for uploadnewmedia.
  name: Orange Logic Upload New Media API
  slug: orangelogic-uploadnewmedia-api
- baseURL: https://{OrangeLogicURL}/webapi
  baseurl_source: declared
  description: The UploadNewVersion API from Orange Logic — 1 operation(s) for uploadnewversion.
  name: Orange Logic Upload New Version API
  slug: orangelogic-uploadnewversion-api
artifact_total: 57
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/agentic-access/orangelogic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orangelogic-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/rules/orangelogic-rules.yml
  title: ''
  type: Spectral
  url: rules/orangelogic-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.orangelogic.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/errors/orangelogic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orangelogic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/conformance/orangelogic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orangelogic-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/llms/orangelogic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orangelogic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/hosts/orangelogic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orangelogic-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/integrations/orangelogic-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/orangelogic-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/vendors/orangelogic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orangelogic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orangelogic.com/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.orangelogic.com/features/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orangelogic.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.orangelogic.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/scopes/orangelogic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/orangelogic-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/authentication/orangelogic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orangelogic-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.orangelogic.com/dam-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.orangelogic.com/dam-blog/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/security/orangelogic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/orangelogic-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/security/orangelogic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orangelogic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange-logic
- group: company
  title: ''
  type: Website
  url: https://www.orangelogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orangelogic.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/plans/orangelogic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orangelogic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/rate-limits/orangelogic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/orangelogic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/finops/orangelogic-finops.yml
  title: ''
  type: FinOps
  url: finops/orangelogic-finops.yml
created: '2026-07-05'
description: Orange Logic builds OrangeDAM (formerly branded Cortex), an enterprise digital asset management (DAM) and media asset management (MAM) platform used by museums, media companies, financial institutions, healthcare, and government archives. OrangeDAM exposes a documented REST API for assets, metadata, search, users, folders, and webhooks. The API is per-instance and customer-gated - every call is made against your own organization's Orange Logic instance host rather than a single shared public gateway, so the base URL is written here as the placeholder https://{OrangeLogicURL}/webapi. Endpoints come in two families - the newer /webapi/ endpoints (each ending in a unique identifier and version, e.g. token_48I_v1) and the legacy /api/ endpoints (with a version number in the path); Orange Logic recommends the /webapi/ family. Responses are JSON or XML. Pricing is enterprise contact-sales only.
finops:
- has_sources: true
  method: generated
  name: Orangelogic Finops
  primary_unit: ''
  service_category: Digital Asset Management
  slug: orangelogic-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orangelogic.png
layout: provider
modified: '2026-10-06'
name: Orange Logic
nav: Providers
network: true
overview: 'Orange Logic publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Search API, Batcheditfields 4FQ V1 API, Batchupsert 4FY V1 API, and 45 more. Tagged areas include Digital Asset Management, Media Asset Management, MAM, Enterprise, and Metadata.


  The Orange Logic catalog on APIs.io includes 1 Spectral governance ruleset.


  Orange Logic''s developer surface includes authentication, engineering blog, documentation, and 22 more developer resources.'
plans:
- name: Orangelogic Plans Pricing
  plan_count: 1
  slug: orangelogic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Orangelogic Rate Limits
  slug: orangelogic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Orange Logic API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 5
  slug: orangelogic-rules
scopes:
- name: Orangelogic Scopes
  scope_count: 0
  slug: orangelogic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 43.9
    developer_ergonomics: 26.2
    discoverability: 80.4
    operational_transparency: 18.4
  previous_composite: 19.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 41
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/orangelogic/refs/heads/main/screenshots/orangelogic-2026-08-07T190828.png
security:
- kind: authentication
  name: Orangelogic Authentication
  slug: orangelogic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Orangelogic Domain Security
  slug: orangelogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Orangelogic Trust Center
  slug: orangelogic-trust-center
  summary_line: HIPAA, GDPR
slug: orangelogic
tags:
- Digital Asset Management
- Media Asset Management
- MAM
- Enterprise
- Metadata
- Archives
website: https://www.orangelogic.com
---
