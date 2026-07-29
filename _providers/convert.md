---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 153
  human_in_the_loop: 5
  name: Convert Agentic Access
  operation_count: 189
  slug: convert-agentic-access
  summary_line: 189 operations · 153 acting · 5 human-in-the-loop
api_count: 33
apis:
- description: Convert Experiences REST API v2 manages accounts, projects, experiments, goals, audiences, locations, reports, and collaborators. Requests are signed via HMAC.
  name: Convert Experiences REST API v2
  slug: convert-rest-api
- description: Account is the entity that contains all data. An account is owned by an user and in which more other users can have different permissions, account wide or at project level
  name: Convert Accounts API
  slug: convert-accounts-api
- description: The AI content API from Convert — 2 operation(s) for ai content.
  name: Convert AI content API
  slug: convert-ai-content-api
- description: API Keys are used to authenticate requests from Server side applications that access this API
  name: Convert API Keys API
  slug: convert-api-keys-api
- description: Audiences let you segment your users in the ways that are important to your business. You can segment by event (e.g., session_start or level_up) and by user property (e.g., Browser/OS, Geo, Language),
  name: Convert Audiences API
  slug: convert-audiences-api
- description: The Bulk API from Convert — 19 operation(s) for bulk.
  name: Convert Bulk API
  slug: convert-bulk-api
- description: Various endpoints that allow Image Assets loaded through Convert's CDN to be managed
  name: Convert Cdn Images API
  slug: convert-cdn-images-api
- description: Convert Experiences organizes customer data into Accounts(which are billable entities) and gives Users access to accounts under different roles. By default the **user that initially setups an account*
  name: Convert Collaborators API
  slug: convert-collaborators-api
- description: 'In order to use the Convert app, user has two options to authenticate requests: * Provide authorization token with each request works best for backend systems * Authenticate once using username/passwo'
  name: Convert Cookie Authentication API
  slug: convert-cookie-authentication-api
- description: Domains define websites which will be used in experiences in your projects.
  name: Convert Domains API
  slug: convert-domains-api
- description: Convert Experience's Sections provides API to update Sections of an experience.
  name: Convert Experience Sections API
  slug: convert-experience-sections-api
- description: Each **Experience** has one or more **Variations** which are presented to different groups of visitor in order to monitor the results of different changes or to personalize visitor's experience
  name: Convert Experience Variations API
  slug: convert-experience-variations-api
- description: Convert Experiences provides a couple different experiences types. A/B, Split URL, Multivariate (MVT), Deploys, A/A and Multi-page (funnel) testing. To learn more, see <a href="https://support.convert
  name: Convert Experiences API
  slug: convert-experiences-api
- description: Endpoints to retrieve heatmap background and overlay images (Convert Signals™). Filters such as device and interaction type are passed in the request body.
  name: Convert Experiences Heatmaps API
  slug: convert-experiences-heatmaps-api
- description: Specification for different reports data that can be retrieved for experiences
  name: Convert Experiences Reports API
  slug: convert-experiences-reports-api
- description: Features can be created only under **Fullstack** Projects
  name: Convert Features API
  slug: convert-features-api
- description: Various endpoints that allow File Assets loaded through Convert's to be managed
  name: Convert Files API
  slug: convert-files-api
- description: Goals measure how well your site fulfills your target objectives. A goal represents a completed activity, called a conversion, that contributes to the success of your business. Examples of goals inclu
  name: Convert Goals API
  slug: convert-goals-api
- description: A hypothesis is an assumption that a proposed change in your website would lead to visitors taking the action that you want them to. Read more information about <a href="https://support.convert.com/hc
  name: Convert Hypotheses API
  slug: convert-hypotheses-api
- description: The Knowledge Bases API from Convert — 7 operation(s) for knowledge bases.
  name: Convert Knowledge Bases API
  slug: convert-knowledge-bases-api
- description: Locations let you target your experiences in the ways that are important to your business.
  name: Convert Locations API
  slug: convert-locations-api
- description: Manage OAuth clients and authorized sessions.
  name: Convert OAuth API
  slug: convert-oauth-api
- description: 'Delegated authorization endpoints for third-party OAuth clients. Typical flow: * OAuth client initiates GET request in browser (`/oauth/authorize`) with `client_id` + `response_type=code` + `scope` + '
  name: Convert OAuth Authorization API
  slug: convert-oauth-authorization-api
- description: The Observations API from Convert — 7 operation(s) for observations.
  name: Convert Observations API
  slug: convert-observations-api
- description: 'Once you start using Convert Experiences, you will have a growing number of experiences to manage. Projects help you keep everything organized across multiple sites. Each project has its own tracking '
  name: Convert Projects API
  slug: convert-projects-api
- description: The SDK Keys API from Convert — 4 operation(s) for sdk keys.
  name: Convert SDK Keys API
  slug: convert-sdk-keys-api
- description: Convert Experience's Versions provides API to update Versions inside an experience's Section
  name: Convert Section Versions API
  slug: convert-section-versions-api
- description: Tags define tag labels for your project.
  name: Convert Tags API
  slug: convert-tags-api
- description: Authenticated user related endpoints
  name: Convert User API
  slug: convert-user-api
- description: Each **Experience's Variation** has one or more **Changes**; a change represent the actual modification that is applied to a visitor. It can be a piece of javascript or CSS code for web experiences or
  name: Convert Version Changes API
  slug: convert-version-changes-api
- description: Endpoints for managing visitor data placeholders personalization data. Visitor data placeholders define dynamic content that can be personalized for individual visitors or groups.
  name: Convert Visitor Data Placeholders API
  slug: convert-visitor-data-placeholders-api
- description: Visitor Insights for the project
  name: Convert Visitor Insights API
  slug: convert-visitor-insights-api
- description: The Visitors Data API from Convert — 7 operation(s) for visitors data.
  name: Convert Visitors Data API
  slug: convert-visitors-data-api
artifact_total: 41
collections:
- collection_type: open
  name: Convert API
  slug: open-convert
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convert-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/convert-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convert-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convert-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.convert.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.convert.com/doc/v2/
- group: commercial
  title: ''
  type: Plans
  url: plans/convert-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/convert-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/convert-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.convert.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.convert.com/blog/feed/
created: '2026-05-08'
description: Convert is an A/B testing and experimentation platform with privacy-first analytics and integrations for marketers and developers.
finops:
- name: Convert Finops
  service_category: A/B Testing
  slug: convert-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convert.png
layout: provider
modified: '2026-05-08'
name: Convert
nav: Providers
network: true
overview: 'Convert publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI content API, API Keys API, and 29 more. Tagged areas include Experimentation, AB Testing, Conversion Optimization, Personalization, and Analytics.


  Convert''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Convert Plans Pricing
  plan_count: 1
  slug: convert-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Convert Rate Limits
  slug: convert-rate-limits
score:
  band: thin
  composite: 33.6
  delta: -1.9
  facets:
    commercial_clarity: 36.8
    contract_quality: 50.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convert/refs/heads/main/screenshots/convert-2026-06-20T174956.png
security:
- kind: authentication
  name: Convert Authentication
  slug: convert-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Convert Domain Security
  slug: convert-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Convert Trust Center
  slug: convert-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: convert
tags:
- Experimentation
- AB Testing
- Conversion Optimization
- Personalization
- Analytics
website: https://www.convert.com/
---
