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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 41
apis:
- description: <a id="group-answers"></a> Answers are the users’ replies to the questions raised by their colleagues in the Questions menu. Other users can vote for answers they think are best, like them, and a user
  name: Yoobic Answers API
  slug: yoobic-answers-api
- description: '<a id="group-badges"></a> A badge is a customized reward earned by a learner after completing a lesson. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |---------------------'
  name: Yoobic Badges API
  slug: yoobic-badges-api
- description: <a id="group-bot_messages"></a> Bot analytics allow you to improve your bots by understanding how your teams use them and how satisfied they are with the answers. The key metrics available can be used
  name: Yoobic Bot Messages API
  slug: yoobic-bot-messages-api
- description: <a id="group-bots"></a> This API is exclusively used to handle bots external to YOOBIC. External bots are an AI feature of the YOOBIC chat that enhances user interactions by automating workflows and s
  name: Yoobic Bots API
  slug: yoobic-bots-api
- description: <a id="group-salesdata"></a> Business KPIs data allows integration of external business data per location. This is the data that will be used to display Business KPIs in the Activity Hub or Today's fo
  name: Yoobic Business KPIs data - salesdata API
  slug: yoobic-business-kpis-data-salesdata-api
- description: <a id="group-campaigns"></a> A campaign is the main structure used to send tasks to frontline teams and collect data about how they execute them. It is essentially a configurable form with instruction
  name: Yoobic Campaigns API
  slug: yoobic-campaigns-api
- description: '<a id="group-catalogs"></a> Holds a list of catalogs and their relevant data. Each catalog contains a list of [`products`](#group-products). ### Fields | Field | Type | Required | Readonly | OrderBy |'
  name: Yoobic Catalogs API
  slug: yoobic-catalogs-api
- description: '<a id="group-chats"></a> Chats are used for internal communication between users directly in the YOOBIC app. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |-------|:----:|:'
  name: Yoobic Chats API
  slug: yoobic-chats-api
- description: '<a id="group-comments"></a> Get all feeds comments. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:--------------:|:--------:|:--------:|:-------:|-'
  name: Yoobic Comments API
  slug: yoobic-comments-api
- description: <a id="group-communities"></a> Communities are a sub-section of the general Newsfeed tab in YOOBIC. Unlike the Newsfeed, where you can read all the posts shared for your company, a community can be na
  name: Yoobic Communities API
  slug: yoobic-communities-api
- description: <a id="group-community-posts"></a> The posts made in the communities appear both in the community newsfeed and in the main newsfeed, along with the posts in the normal newsfeed (unless otherwise confi
  name: Yoobic Community Posts API
  slug: yoobic-community-posts-api
- description: '<a id="group-competencies"></a> A competency of a course allows measuring the success rate of a learner on all courses linked to that competency. Each course can be linked to only one competency. ### '
  name: Yoobic Competencies API
  slug: yoobic-competencies-api
- description: '<a id="group-course-categories"></a> Category in courses allows grouping available courses by topics or themes in the Discover section of the app. Each course can be linked to only one category. ### F'
  name: Yoobic Course Categories API
  slug: yoobic-course-categories-api
- description: '<a id="group-courses"></a> When a plan is assigned to a user it creates a course. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:--------------:|:--'
  name: Yoobic Courses API
  slug: yoobic-courses-api
- description: '<a id="group-custom_model_instances"></a> Datasets are where all your data is stored. They have some similarities to spreadsheets, for example they look similar and support some of the same functions '
  name: Yoobic Custom Model Instances - Datasets API
  slug: yoobic-custom-model-instances-datasets-api
- description: '<a id="group-events"></a> Events can be created and managed through the YOOBIC app and are displayed in the calendar. Events can be public (visible to all users sharing at least one group with it) or '
  name: Yoobic Events API
  slug: yoobic-events-api
- description: '<a id="group-files"></a> Files provides information about the external files used in the application. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|'
  name: Yoobic Files API
  slug: yoobic-files-api
- description: '<a id="group-geofilters"></a> provides a mapping between users and the stores they have permission to visit - Each user may have more than one store mapped. If enabled, users could only book missions '
  name: Yoobic Geofilters API
  slug: yoobic-geofilters-api
- description: <a id="group-groups"></a> Groups are used to manage users. This is VERY important as Groups are what make using the application much simpler. By adding Users to Groups, when you need to modify sets of
  name: Yoobic Groups API
  slug: yoobic-groups-api
- description: <a id="group-incentives-kpi"></a> Incentives-KPIs are an indicator for users’ progress within an incentive. Each incentives-kpi represents the sale of one or more items of a single product. When a use
  name: Yoobic Incentives Kpi API
  slug: yoobic-incentives-kpi-api
- description: <a id="group-inventory"></a> An Inventory is a custom data structure to manage and use data in a similar way as in a spreadsheet or database directly from the YOOBIC Platform. Each inventory has a def
  name: Yoobic Inventory API
  slug: yoobic-inventory-api
- description: <a id="group-jobs"></a> The Jobs endpoint allows you to query the status of your asynchronous jobs, whether they are queued, running, completed, or expired. The `id` required to request status is retu
  name: Yoobic Jobs API
  slug: yoobic-jobs-api
- description: '<a id="group-lessons"></a> Lessons are the activities the users perform during their trainings. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:-----'
  name: Yoobic Lessons API
  slug: yoobic-lessons-api
- description: '<a id="group-mission_comments"></a> Perform operations on comments linked to missions. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:--------------'
  name: Yoobic Mission Comments API
  slug: yoobic-mission-comments-api
- description: <a id="group-missions"></a> Missions are the basic campaign type. The store users will receive missions with fields to complete, for example send a photo of their display or change the location of the
  name: Yoobic Missions API
  slug: yoobic-missions-api
- description: '<a id="group-news"></a> Contains information coming from the news feed tab ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:--------------:|:--------:'
  name: Yoobic News API
  slug: yoobic-news-api
- description: '<a id="group-notifications"></a> Notifications provide information about the internal notifications sent to users in the application. ### Fields | Field | Type | Required | Readonly | OrderBy | Descri'
  name: Yoobic Notifications API
  slug: yoobic-notifications-api
- description: '<a id="group-photos"></a> contains information about uploaded photos and photos taken as part of a mission and its relations to the mission. ### Fields | Field | Type | Required | Readonly | OrderBy |'
  name: Yoobic Photos API
  slug: yoobic-photos-api
- description: '<a id="group-plans"></a> A plan is the main description of a course that''s assigned to users. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:-------'
  name: Yoobic Plans API
  slug: yoobic-plans-api
- description: '<a id="group-products"></a> Products represent usually physical products and are organised by [`catalog`](#group-catalogs) ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |--'
  name: Yoobic Products API
  slug: yoobic-products-api
- description: <a id="group-questions"></a> Questions are a Social Learning feature, allowing users to learn tips / expertise from each other. They can ask questions and others can reply to them. Admins and managers
  name: Yoobic Questions API
  slug: yoobic-questions-api
- description: <a id="group-roles"></a> Get the list of Roles available for the users in your organization. The roles are defined by a combination of `client_role` and `client_role_extension` The `client_role` refer
  name: Yoobic Roles API
  slug: yoobic-roles-api
- description: <a id="group-security"></a> This endpoint exposes the login method in order to create a valid access token for subsequents call to the API, as well as an endpoint for invalidating the current access t
  name: Yoobic Security API
  slug: yoobic-security-api
- description: <a id="group-shifts"></a> A shift object represents a scheduled period of time in which a specific employee is expected to work at a specific store. The object includes information about the start and
  name: Yoobic Shifts API
  slug: yoobic-shifts-api
- description: <a id="group-store_types"></a> Stores always belong to specific Store Type. Store Types determine which stores users can potentially see. They will be linked to one or several user groups. Store types
  name: Yoobic Store Types API
  slug: yoobic-store-types-api
- description: <a id="group-stores"></a> Stores are a very important part of the application. They represent physical locations of stores. They are the entities which receive missions (not the users). The users asso
  name: Yoobic Stores API
  slug: yoobic-stores-api
- description: '<a id="group-tenants"></a> Exposes tenant level information. ### Fields | Field | Type | Required | Readonly | OrderBy | Description | |----------------------|:--------------:|:--------:|:--------:|:-'
  name: Yoobic Tenants API
  slug: yoobic-tenants-api
- description: '<a id="group-translations"></a> Contains translations of common keys used in the app to different languages. ### Table Translations | Field | Type | Required | Readonly | OrderBy | Description | |----'
  name: Yoobic Translations API
  slug: yoobic-translations-api
- description: '<a id="group-users"></a> Expose users for your company. Remember: - Users are the people at your company with access to the YOOBIC mobile and/or web apps. - Users can be assigned to one or more groups'
  name: Yoobic Users API
  slug: yoobic-users-api
- description: '<a id="group-visits"></a> Through this endpoint the details and/or the approval of the visit could be set. By default, the visits will be shown as pending until they are approved (`compliant`). Below '
  name: Yoobic Visits API
  slug: yoobic-visits-api
- description: '<a id="group-webhooks"></a> You can create webhooks with HTTP targets to build integrations with the services or with your back-end system. Examples: - Alert your team in Slack when a mission is creat'
  name: Yoobic Webhooks API
  slug: yoobic-webhooks-api
artifact_total: 45
asyncapis:
- description: ''
  name: Yoobic Webhooks
  slug: yoobic-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.yoobic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yoobic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yoobic.com/api.html
- group: company
  title: ''
  type: Blog
  url: https://yoobic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yoobic
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yoobic.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://yoobic.com/book-a-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.yoobic.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@yoobic.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yoobic.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yoobic-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yoobic-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yoobic-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yoobic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/yoobic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/yoobic-trust-center.yml
created: '2026-07-17'
description: YOOBIC is an AI-powered frontline employee experience and retail operations platform that unifies task management, internal communications, and mobile microlearning, giving headquarters real-time visibility and frontline teams the tools to execute in-store. It serves retail, grocery, fashion and luxury, convenience, pharmacy, restaurant/QSR, and fitness brands. The YOOBIC Public API is a RESTful JSON API (OpenAPI 3.0, 230 paths / 265 operations across 41 resource groups) for programmatically managing users, stores, missions, campaigns, learning, communities, and webhooks, secured with JWT bearer tokens.
image: https://yoobic.com/wp-content/uploads/2025/11/cropped-favicon-1-1-270x270.png
layout: provider
modified: '2026-07-21'
name: Yoobic
nav: Providers
network: true
overview: 'Yoobic publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Badges API, Bot Messages API, and 38 more. Tagged areas include Company, Retail, Frontline Operations, Task Management, and Workforce.


  The Yoobic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yoobic''s developer surface includes documentation, engineering blog, pricing, signup flow, support, authentication, and 10 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 42.7
  delta: -1.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 44.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yoobic Authentication
  slug: yoobic-authentication
  summary_line: http-bearer · 2 schemes
- kind: domain-security
  name: Yoobic Domain Security
  slug: yoobic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yoobic Trust Center
  slug: yoobic-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: yoobic
tags:
- Company
- Retail
- Frontline Operations
- Task Management
- Workforce
- Microlearning
- Employee Experience
- REST
- Webhooks
- SCIM
website: https://www.yoobic.com/
---
