---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 6
apis:
- description: 'Query Brandwatch''s content library or imported data to return aggregated statistics and computed analysis. Enables programmatic access to brand mention analytics, sentiment scores, volume trends, and '
  name: Brandwatch Analysis API
  slug: analysis-api
- description: Import unstructured data from any source for analysis alongside consumer conversation data. Enables organizations to blend proprietary data with Brandwatch's social intelligence for unified analytics.
  name: Brandwatch Data Upload API
  slug: data-upload-api
- description: Export analysis results for further research and integration with existing systems. Supports real-time data streaming alongside consumer conversation data for continuous monitoring and research workfl
  name: Brandwatch Consumer Research API
  slug: consumer-research-api
- description: Integrate owned social media metrics into external analytics solutions for custom reporting. Enables organizations to combine their social channel performance data with Brandwatch's audience intellige
  name: Brandwatch Measure API
  slug: measure-api
- description: Export social publishing data to integrate with content management systems. Enables workflow automation between Brandwatch's publishing tools and external CMS platforms for unified content operations.
  name: Brandwatch Publish API
  slug: publish-api
- description: Consolidate conversations from social media inboxes with customer inquiries across platforms. Enables integration of Brandwatch's engagement tools with CRM and customer service systems for unified con
  name: Brandwatch Engage API
  slug: engage-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandwatch-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandwatchltd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandwatch
- group: company
  title: ''
  type: Website
  url: https://www.brandwatch.com
- group: other
  title: ''
  type: APIProducts
  url: https://www.brandwatch.com/products/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brandwatch.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.brandwatch.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.brandwatch.com/blog/feed/
created: '2025-03-01'
description: Brandwatch is a leading consumer intelligence and social media analytics platform providing access to trillions of consumer conversations. The platform offers six distinct APIs for analysis, data upload, consumer research, social metrics, publishing, and engagement. Businesses use Brandwatch to track brand mentions, monitor competitors, analyze sentiment, and integrate social data with existing analytics and CRM systems for strategic decision-making.
finops:
- name: Brandwatch Finops
  service_category: API
  slug: brandwatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brandwatch.png
layout: provider
modified: '2026-04-21'
name: Brandwatch
nav: Providers
network: true
overview: 'Brandwatch publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Social Media, Social Media Monitoring, Consumer Intelligence, and Brand Management.


  Brandwatch''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Brandwatch Plans Pricing
  plan_count: 3
  slug: brandwatch-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Brandwatch Rate Limits
  slug: brandwatch-rate-limits
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandwatch/refs/heads/main/screenshots/brandwatch-2026-06-20T173633.png
security:
- kind: domain-security
  name: Brandwatch Domain Security
  slug: brandwatch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brandwatch
tags:
- Analytics
- Social Media
- Social Media Monitoring
- Consumer Intelligence
- Brand Management
- Sentiment Analysis
website: https://www.brandwatch.com
---
