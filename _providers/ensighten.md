---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 26.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: Requests using a username and password for authentication follow the Resource Owner Password Flow of the OAuth 2.0 specification. API Request Once a token has been retrieved using the /auth/token proc
  name: Ensighten Authentication API
  slug: ensighten-authentication-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Conditions. Important Condition specific fields Field Description Valid Values id The condition id name The name of the condition A name up to 255 characters conditionValues Crite
  name: Ensighten Conditions API
  slug: ensighten-conditions-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: 'CRUD operations with Data Definitions. Data Definitions specific fields Field Required Description Valid Values name Y The name of the definition A name up to 255 characters collection Y The name for '
  name: Ensighten Data Definitions API
  slug: ensighten-data-definitions-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Deployments. Important Deployment specific fields Field Description Valid Values id The deployment id name The name of the deployment A name up to 255 characters spaceId The id of
  name: Ensighten Deployments API
  slug: ensighten-deployments-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Event Definitions. Event Definition specific fields Field Description Valid Values name The name of the definition A name up to 255 characters type Indicates the type of the event
  name: Ensighten Event Definitions API
  slug: ensighten-event-definitions-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: Operations specific to Git enabled spaces. Git specific fields Field Description Valid Values commitId Commit ID A SHA-1 hash, 40 characters long
  name: Ensighten GIT API
  slug: ensighten-git-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Labels. Label specific fields Field Description Valid Values key The key of the label A string up to 128 characters. Should only contain alphanumerics (a-z, A-Z, 0-9), periods, +,
  name: Ensighten Labels API
  slug: ensighten-labels-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Publish Paths. For further details or guidance on configuring Publish Path settings, please consult our Help Center article available here. Publish Path specific fields Field Requ
  name: Ensighten Publish Paths API
  slug: ensighten-publish-paths-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Roles. Role specific fields Field Description Valid Values name Unique identifier for the role Up to 255 characters; Role name should only contain alphanumerics (a-z, A-Z, 0-9), p
  name: Ensighten Roles API
  slug: ensighten-roles-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: SCIM2 (System for Cross-domain Identity Management) is a specification that automates user and group identity provisioning across cloud-based applications and services using SSO and Identity Providers
  name: Ensighten SCIM 2.0 API
  slug: ensighten-scim-2-0-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Spaces. Space specific fields Field Required Description Valid Values name Y The name of the space A name up to 255 characters publishPaths Y A list of either existing paths (prov
  name: Ensighten Spaces API
  slug: ensighten-spaces-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: 'Retrieve TDN job information JSON Schema Conforms to JSON schema draft v4 specifications { "$schema": "http://json-schema.org/draft-04/schema#", "description": "Get job response", "type": "object", "p'
  name: Ensighten TDN API
  slug: ensighten-tdn-api
- baseURL: https://manage-api.ensighten.com
  baseurl_source: declared
  description: CRUD operations with Users. User specific fields Field Description Valid Values username Unique identifier for the user Up to 255 characters; cannot include <, >, :, ~, +, or spaces firstName User's f
  name: Ensighten Users API
  slug: ensighten-users-api
artifact_total: 18
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ensighten-manage-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cheq.ai/ensighten/
- group: start
  title: ''
  type: Login
  url: https://manage.ensighten.com/
- group: operate
  title: ''
  type: Support
  url: https://help.ensighten.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ensighten.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://cheq.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheq.ai/cheq-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheq.ai/website-privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://cheq.ai/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://cheq.ai/trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ensighten-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ensighten-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://manageexternalapi.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://manageexternalapi.docs.apiary.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ensighten.com/hc/en-us/sections/22957479812369
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ensighten
- group: build
  title: ''
  type: Packages
  url: packages/ensighten-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ensighten-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ensighten-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ensighten-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ensighten-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ensighten-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ensighten-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ensighten-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ensighten-data-model.yml
created: '2026-07-17'
description: 'Ensighten is an enterprise tag management, data governance, and client-side website security platform. It gives digital, marketing, and privacy teams centralized control over the third-party tags, scripts, and vendor code that run on their web and mobile properties, enforcing consent and privacy rules (GDPR, CCPA) at the point of data collection. The platform combines server- and client-side tag management, malicious-script and data-leakage detection (client-side security), and consent management. Ensighten was acquired by CHEQ (CHEQ AI Technologies Ltd.) and is now delivered as part of CHEQ''s Control & Compliance / Go-to-Market Security suite; the ensighten.com domain 301-redirects to cheq.ai. This company profile was surfaced as an Insight Partners portfolio lead and enriched by the API Evangelist pipeline. Ensighten does publish a public REST contract: the Ensighten Manage API, documented as an API Blueprint at manageexternalapi.docs.apiary.io and served in production from
  manage-api.ensighten.com. It covers 66 operations across Spaces, Publish Paths, Deployments, Conditions, Data Definitions, Event Definitions, Labels, Users, Roles, SCIM 2.0 user/group provisioning, Git-enabled spaces, and TDN jobs. Authentication is either an X-API-Key API key or an OAuth 2.0 Resource Owner Password Credentials bearer token from /auth/token.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ensighten.png
layout: provider
modified: '2026-08-13'
name: Ensighten
nav: Providers
network: true
overview: 'Ensighten publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Conditions API, Data Definitions API, and 10 more. Tagged areas include Company, Cybersecurity, Tag Management, Data Governance, and Client-Side Security.


  Ensighten''s developer surface includes support, engineering blog, documentation, API reference, getting-started guide, changelog, and 20 more developer resources.'
plans:
- name: Ensighten Plans Pricing
  plan_count: 0
  slug: ensighten-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Ensighten Rate Limits
  slug: ensighten-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 18.6
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 40.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ensighten/refs/heads/main/screenshots/ensighten-2026-07-25T213419.png
security:
- kind: authentication
  name: Ensighten Authentication
  slug: ensighten-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Ensighten Domain Security
  slug: ensighten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ensighten Trust Center
  slug: ensighten-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, ISO 42001, CSA STAR Level 1, GDPR, CCPA
slug: ensighten
tags:
- Company
- Cybersecurity
- Tag Management
- Data Governance
- Client-Side Security
- Consent Management
- Privacy Compliance
- Marketing Technology
website: https://cheq.ai/ensighten/
---
