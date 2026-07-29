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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 73
  human_in_the_loop: 1
  name: Netlify Agentic Access
  operation_count: 133
  slug: netlify-agentic-access
  summary_line: 133 operations · 73 acting · 1 human-in-the-loop
api_count: 35
apis:
- description: The accessToken API from Netlify — 1 operation(s) for accesstoken.
  name: Netlify accessToken API
  slug: netlify-accesstoken-api
- description: The accountMembership API from Netlify — 2 operation(s) for accountmembership.
  name: Netlify accountMembership API
  slug: netlify-accountmembership-api
- description: The accountType API from Netlify — 1 operation(s) for accounttype.
  name: Netlify accountType API
  slug: netlify-accounttype-api
- description: The Asset API from Netlify — 2 operation(s) for asset.
  name: Netlify Asset API
  slug: netlify-asset-api
- description: The assetPublicSignature API from Netlify — 1 operation(s) for assetpublicsignature.
  name: Netlify assetPublicSignature API
  slug: netlify-assetpublicsignature-api
- description: The auditLog API from Netlify — 1 operation(s) for auditlog.
  name: Netlify auditLog API
  slug: netlify-auditlog-api
- description: The Build API from Netlify — 4 operation(s) for build.
  name: Netlify Build API
  slug: netlify-build-api
- description: The buildHook API from Netlify — 2 operation(s) for buildhook.
  name: Netlify buildHook API
  slug: netlify-buildhook-api
- description: The buildLogMsg API from Netlify — 1 operation(s) for buildlogmsg.
  name: Netlify buildLogMsg API
  slug: netlify-buildlogmsg-api
- description: The Deploy API from Netlify — 8 operation(s) for deploy.
  name: Netlify Deploy API
  slug: netlify-deploy-api
- description: The deployedBranch API from Netlify — 1 operation(s) for deployedbranch.
  name: Netlify deployedBranch API
  slug: netlify-deployedbranch-api
- description: The deployKey API from Netlify — 2 operation(s) for deploykey.
  name: Netlify deployKey API
  slug: netlify-deploykey-api
- description: The devServer API from Netlify — 3 operation(s) for devserver.
  name: Netlify devServer API
  slug: netlify-devserver-api
- description: The devServerHook API from Netlify — 2 operation(s) for devserverhook.
  name: Netlify devServerHook API
  slug: netlify-devserverhook-api
- description: The dnsZone API from Netlify — 6 operation(s) for dnszone.
  name: Netlify dnsZone API
  slug: netlify-dnszone-api
- description: The environmentVariables API from Netlify — 4 operation(s) for environmentvariables.
  name: Netlify environmentVariables API
  slug: netlify-environmentvariables-api
- description: The File API from Netlify — 3 operation(s) for file.
  name: Netlify File API
  slug: netlify-file-api
- description: The Form API from Netlify — 2 operation(s) for form.
  name: Netlify Form API
  slug: netlify-form-api
- description: The Function API from Netlify — 2 operation(s) for function.
  name: Netlify Function API
  slug: netlify-function-api
- description: The Hook API from Netlify — 3 operation(s) for hook.
  name: Netlify Hook API
  slug: netlify-hook-api
- description: The hookType API from Netlify — 1 operation(s) for hooktype.
  name: Netlify hookType API
  slug: netlify-hooktype-api
- description: The Member API from Netlify — 2 operation(s) for member.
  name: Netlify Member API
  slug: netlify-member-api
- description: The Metadata API from Netlify — 1 operation(s) for metadata.
  name: Netlify Metadata API
  slug: netlify-metadata-api
- description: The paymentMethod API from Netlify — 1 operation(s) for paymentmethod.
  name: Netlify paymentMethod API
  slug: netlify-paymentmethod-api
- description: The Purge API from Netlify — 1 operation(s) for purge.
  name: Netlify Purge API
  slug: netlify-purge-api
- description: The serviceInstance API from Netlify — 3 operation(s) for serviceinstance.
  name: Netlify serviceInstance API
  slug: netlify-serviceinstance-api
- description: The Services API from Netlify — 3 operation(s) for services.
  name: Netlify Services API
  slug: netlify-services-api
- description: The Site API from Netlify — 4 operation(s) for site.
  name: Netlify Site API
  slug: netlify-site-api
- description: The sniCertificate API from Netlify — 1 operation(s) for snicertificate.
  name: Netlify sniCertificate API
  slug: netlify-snicertificate-api
- description: The Snippet API from Netlify — 2 operation(s) for snippet.
  name: Netlify Snippet API
  slug: netlify-snippet-api
- description: The splitTest API from Netlify — 4 operation(s) for splittest.
  name: Netlify splitTest API
  slug: netlify-splittest-api
- description: The Submission API from Netlify — 3 operation(s) for submission.
  name: Netlify Submission API
  slug: netlify-submission-api
- description: The Ticket API from Netlify — 2 operation(s) for ticket.
  name: Netlify Ticket API
  slug: netlify-ticket-api
- description: The User API from Netlify — 1 operation(s) for user.
  name: Netlify User API
  slug: netlify-user-api
- description: The X-Internal API from Netlify — 3 operation(s) for x-internal.
  name: Netlify X-Internal API
  slug: netlify-x-internal-api
artifact_total: 170
asyncapis:
- description: 'AsyncAPI description of Netlify''s asynchronous event surface. Two documented surfaces are modelled here: 1. Outgoing webhooks (deploy / form / split test notifications). Netlify issues an HTTP POST to'
  name: Netlify Webhooks and Build Hooks
  slug: netlify-webhooks-asyncapi
collections:
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken API
  slug: postman-netlify-accesstoken-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken accountMembership API
  slug: postman-netlify-accountmembership-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken accountType API
  slug: postman-netlify-accounttype-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Asset API
  slug: postman-netlify-asset-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken assetPublicSignature API
  slug: postman-netlify-assetpublicsignature-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken auditLog API
  slug: postman-netlify-auditlog-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Build API
  slug: postman-netlify-build-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken buildHook API
  slug: postman-netlify-buildhook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken buildLogMsg API
  slug: postman-netlify-buildlogmsg-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Deploy API
  slug: postman-netlify-deploy-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken deployedBranch API
  slug: postman-netlify-deployedbranch-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken deployKey API
  slug: postman-netlify-deploykey-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken devServer API
  slug: postman-netlify-devserver-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken devServerHook API
  slug: postman-netlify-devserverhook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken dnsZone API
  slug: postman-netlify-dnszone-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken environmentVariables API
  slug: postman-netlify-environmentvariables-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken File API
  slug: postman-netlify-file-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Form API
  slug: postman-netlify-form-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Function API
  slug: postman-netlify-function-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Hook API
  slug: postman-netlify-hook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken hookType API
  slug: postman-netlify-hooktype-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Member API
  slug: postman-netlify-member-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Metadata API
  slug: postman-netlify-metadata-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken paymentMethod API
  slug: postman-netlify-paymentmethod-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Purge API
  slug: postman-netlify-purge-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken serviceInstance API
  slug: postman-netlify-serviceinstance-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Services API
  slug: postman-netlify-services-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Site API
  slug: postman-netlify-site-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken sniCertificate API
  slug: postman-netlify-snicertificate-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Snippet API
  slug: postman-netlify-snippet-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken splitTest API
  slug: postman-netlify-splittest-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Submission API
  slug: postman-netlify-submission-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Ticket API
  slug: postman-netlify-ticket-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken User API
  slug: postman-netlify-user-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken X-Internal API
  slug: postman-netlify-x-internal-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/netlify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netlify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/netlify-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netlify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netlify-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/netlify-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netlify
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netlify.com/legal/terms-of-use/
- group: company
  title: ''
  type: Blog
  url: https://netlify.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://netlify.com/changelog/
- group: operate
  title: ''
  type: Change Log RSS
  url: https://www.netlify.com/changelog/feed.xml
- group: operate
  title: ''
  type: Forums
  url: https://answers.netlify.com/
- group: operate
  title: ''
  type: Support
  url: https://www.netlify.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netlify.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://app.netlify.com/signup
- group: start
  title: ''
  type: Portal
  url: https://app.netlify.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.netlifystatus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netlify.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netlify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netlify.com/start/get-started-guide/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netlify
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/netlify/open-api
- group: build
  title: ''
  type: CLI Repository
  url: https://github.com/netlify/cli
- group: docs
  title: ''
  type: CLI Documentation
  url: https://cli.netlify.com/
- group: build
  title: ''
  type: SDKs
  url: https://developers.netlify.com/sdk/
- group: company
  title: ''
  type: About
  url: https://www.netlify.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.netlify.com/contact/
- group: auth
  title: ''
  type: Security
  url: https://www.netlify.com/security/
- group: auth
  title: ''
  type: GDPR Policy
  url: https://www.netlify.com/gdpr-ccpa/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/netlify
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/netlify/netlify-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.netlify.com/llms.txt
created: '2023-11-14'
description: Netlify is a cloud platform for building, deploying, and scaling modern web applications with continuous deployment, serverless functions, and edge computing capabilities.
features:
- 'Free: 300 credits/mo, unlimited deploy previews, global CDN'
- 'Personal at $9/mo: 1,000 credits, smart secret detection'
- 'Pro at $20/mo: 3,000 credits, 3+ concurrent builds, private repos'
- 'Enterprise custom: unlimited credits, 99.99% SLA, SSO/SCIM'
- REST API at api.netlify.com
- 'Open API: 500 req/min/token rate limit'
- 'Deploy creates: 3/min/site'
- 'Build concurrency: 1 Free/Personal, 3 Pro'
- Edge Functions (Deno runtime)
- Functions (Node serverless)
- Netlify Forms
- Netlify Identity / Auth
- Netlify Database (Postgres)
- Netlify Blobs (object store)
- Image CDN with transformations
- Webhooks for build events
finops:
- name: Netlify Finops
  service_category: Edge Hosting
  slug: netlify-finops
graphqls:
- description: Netlify offered a GraphQL API through its Netlify Graph developer preview (built on the OneGraph platform, which Netlify acquired in 2021). The API was accessible at `https://graph.netlify.com/graphql
  name: Netlify GraphQL API
  slug: netlify-graphql
image: https://www.netlify.com/v3/img/components/logomark.png
json_schemas:
- name: accessToken
  property_count: 5
  slug: netlify-accesstoken
- name: accountAddMemberSetup
  property_count: 2
  slug: netlify-accountaddmembersetup
- name: accountMembership
  property_count: 16
  slug: netlify-accountmembership
- name: accountSetup
  property_count: 5
  slug: netlify-accountsetup
- name: accountType
  property_count: 8
  slug: netlify-accounttype
- name: accountUpdateMemberSetup
  property_count: 3
  slug: netlify-accountupdatemembersetup
- name: accountUpdateSetup
  property_count: 7
  slug: netlify-accountupdatesetup
- name: accountUsageCapability
  property_count: 2
  slug: netlify-accountusagecapability
- name: asset
  property_count: 12
  slug: netlify-asset
- name: assetForm
  property_count: 2
  slug: netlify-assetform
- name: assetPublicSignature
  property_count: 1
  slug: netlify-assetpublicsignature
- name: assetSignature
  property_count: 2
  slug: netlify-assetsignature
- name: auditLog
  property_count: 3
  slug: netlify-auditlog
- name: build
  property_count: 6
  slug: netlify-build
- name: buildHook
  property_count: 6
  slug: netlify-buildhook
- name: buildHookSetup
  property_count: 2
  slug: netlify-buildhooksetup
- name: buildLogMsg
  property_count: 3
  slug: netlify-buildlogmsg
- name: buildSetup
  property_count: 2
  slug: netlify-buildsetup
- name: buildStatus
  property_count: 5
  slug: netlify-buildstatus
- name: deploy
  property_count: 30
  slug: netlify-deploy
- name: deployedBranch
  property_count: 6
  slug: netlify-deployedbranch
- name: deployFiles
  property_count: 9
  slug: netlify-deployfiles
- name: deployKey
  property_count: 3
  slug: netlify-deploykey
- name: devServer
  property_count: 12
  slug: netlify-devserver
- name: devServerHook
  property_count: 7
  slug: netlify-devserverhook
- name: devServerHookSetup
  property_count: 3
  slug: netlify-devserverhooksetup
- name: dnsRecord
  property_count: 11
  slug: netlify-dnsrecord
- name: dnsRecordCreate
  property_count: 9
  slug: netlify-dnsrecordcreate
- name: dnsRecords
  property_count: 0
  slug: netlify-dnsrecords
- name: dnsZone
  property_count: 16
  slug: netlify-dnszone
- name: dnsZones
  property_count: 0
  slug: netlify-dnszones
- name: dnsZoneSetup
  property_count: 3
  slug: netlify-dnszonesetup
- name: envVar
  property_count: 6
  slug: netlify-envvar
- name: envVarUser
  property_count: 4
  slug: netlify-envvaruser
- name: envVarValue
  property_count: 4
  slug: netlify-envvarvalue
- name: error
  property_count: 2
  slug: netlify-error
- name: excludedFunctionRoute
  property_count: 3
  slug: netlify-excludedfunctionroute
- name: file
  property_count: 5
  slug: netlify-file
- name: form
  property_count: 7
  slug: netlify-form
- name: function
  property_count: 3
  slug: netlify-function
- name: functionConfig
  property_count: 7
  slug: netlify-functionconfig
- name: functionRoute
  property_count: 5
  slug: netlify-functionroute
- name: functionSchedule
  property_count: 2
  slug: netlify-functionschedule
- name: hook
  property_count: 8
  slug: netlify-hook
- name: hookType
  property_count: 3
  slug: netlify-hooktype
- name: member
  property_count: 5
  slug: netlify-member
- name: metadata
  property_count: 0
  slug: netlify-metadata
- name: paymentMethod
  property_count: 7
  slug: netlify-paymentmethod
- name: plugin
  property_count: 2
  slug: netlify-plugin
- name: pluginParams
  property_count: 1
  slug: netlify-pluginparams
- name: pluginRun
  property_count: 0
  slug: netlify-pluginrun
- name: pluginRunData
  property_count: 7
  slug: netlify-pluginrundata
- name: purge
  property_count: 3
  slug: netlify-purge
- name: repoInfo
  property_count: 15
  slug: netlify-repoinfo
- name: service
  property_count: 13
  slug: netlify-service
- name: serviceInstance
  property_count: 12
  slug: netlify-serviceinstance
- name: site
  property_count: 35
  slug: netlify-site
- name: siteFunction
  property_count: 6
  slug: netlify-sitefunction
- name: siteSetup
  property_count: 0
  slug: netlify-sitesetup
- name: sniCertificate
  property_count: 5
  slug: netlify-snicertificate
- name: snippet
  property_count: 7
  slug: netlify-snippet
- name: splitTest
  property_count: 9
  slug: netlify-splittest
- name: splitTests
  property_count: 0
  slug: netlify-splittests
- name: splitTestSetup
  property_count: 1
  slug: netlify-splittestsetup
- name: submission
  property_count: 12
  slug: netlify-submission
- name: ticket
  property_count: 4
  slug: netlify-ticket
- name: trafficRulesAggregateConfig
  property_count: 1
  slug: netlify-trafficrulesaggregateconfig
- name: trafficRulesConfig
  property_count: 1
  slug: netlify-trafficrulesconfig
- name: trafficRulesRateLimitConfig
  property_count: 3
  slug: netlify-trafficrulesratelimitconfig
- name: user
  property_count: 11
  slug: netlify-user
json_structures:
- name: Netlify Structure
  property_count: 0
  slug: netlify-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Netlify
nav: Providers
network: true
overview: 'Netlify publishes 35 APIs on the [APIs.io](https://apis.io/) network, including accessToken API, accountMembership API, accountType API, and 32 more. Tagged areas include CDN, Cloud, Continuous Deployment, Edge Computing, and JAMstack.


  The Netlify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Netlify''s developer surface includes authentication, engineering blog, changelog, support, signup flow, developer portal, pricing, and 26 more developer resources.'
plans:
- name: Netlify Plans Pricing
  plan_count: 4
  slug: netlify-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 4
  name: Netlify Rate Limits
  slug: netlify-rate-limits
rules:
- name: Netlify API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: netlify-asyncapi-spectral-rules
- name: Netlify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: netlify-jsonschema-spectral-rules
scopes:
- name: Netlify Scopes
  scope_count: 0
  slug: netlify-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.4
  delta: -1.1
  facets:
    commercial_clarity: 78.9
    contract_quality: 57.5
    developer_ergonomics: 65.2
    discoverability: 59.3
    governance: 41.7
    operational_transparency: 78.9
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netlify/refs/heads/main/screenshots/netlify-2026-06-20T190259.png
security:
- kind: authentication
  name: Netlify Authentication
  slug: netlify-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Netlify Domain Security
  slug: netlify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Netlify Trust Center
  slug: netlify-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, PCI DSS, HIPAA, GDPR
slug: netlify
tags:
- CDN
- Cloud
- Continuous Deployment
- Edge Computing
- JAMstack
- Serverless
- Serverless Functions
- Static Sites
- Web Hosting
- Websites
website: https://app.netlify.com/
---
