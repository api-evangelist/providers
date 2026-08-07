---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 2
  name: Linkedin Agentic Access
  operation_count: 148
  slug: linkedin-agentic-access
  summary_line: 148 operations · 62 acting · 2 human-in-the-loop
api_count: 65
apis:
- description: The LinkedIn Consumer Solutions Platform enables sites and applications the power to enhance their sign-in experience using the world's largest professional network. The Consumer Solutions Platform co
  name: LinkedIn Consumer API
  slug: linkedin-consumer-api
- description: Manage entity ACLs and assignees
  name: LinkedIn Access Control API
  slug: linkedin-access-control-api
- description: APIs to create and manage ad accounts
  name: LinkedIn Account Management API
  slug: linkedin-account-management-api
- description: APIs to retrieve and manage ad accounts
  name: LinkedIn Ad Accounts API
  slug: linkedin-ad-accounts-api
- description: APIs to discover and retrieve ad targeting facets and entities
  name: LinkedIn Ad Targeting Entities API
  slug: linkedin-ad-targeting-entities-api
- description: Operations for retrieving advertiser transparency data for sponsored accounts
  name: LinkedIn Advertiser Transparency API
  slug: linkedin-advertiser-transparency-api
- description: APIs for retrieving child application details
  name: LinkedIn Application Retrieval API
  slug: linkedin-application-retrieval-api
- description: Sync job applications and related data
  name: LinkedIn Application Synchronization API
  slug: linkedin-application-synchronization-api
- description: APIs for updating child application configurations
  name: LinkedIn Application Updates API
  slug: linkedin-application-updates-api
- description: APIs for creating and managing Apply Connect enabled job postings
  name: LinkedIn Apply Connect Jobs API
  slug: linkedin-apply-connect-jobs-api
- description: APIs to retrieve audience counts based on targeting criteria
  name: LinkedIn Audience Counts API
  slug: linkedin-audience-counts-api
- description: APIs to fetch audience insights based on targeting criteria
  name: LinkedIn Audience Insights API
  slug: linkedin-audience-insights-api
- description: OAuth 2.0 token management for customer applications
  name: LinkedIn Authentication API
  slug: linkedin-authentication-api
- description: Business manager account relationships
  name: LinkedIn Business Manager API
  slug: linkedin-business-manager-api
- description: APIs to create and manage campaign groups
  name: LinkedIn Campaign Group Management API
  slug: linkedin-campaign-group-management-api
- description: APIs to create and manage campaigns
  name: LinkedIn Campaign Management API
  slug: linkedin-campaign-management-api
- description: Sync candidate data from ATS to LinkedIn
  name: LinkedIn Candidate Synchronization API
  slug: linkedin-candidate-synchronization-api
- description: APIs for provisioning and managing customer (child) applications
  name: LinkedIn Child Application Provisioning API
  slug: linkedin-child-application-provisioning-api
- description: APIs to stream company data for account targeting
  name: LinkedIn Company Streaming API
  slug: linkedin-company-streaming-api
- description: APIs to opt-in and opt-out members for compliance monitoring on LinkedIn
  name: LinkedIn Compliance Authorization API
  slug: linkedin-compliance-authorization-api
- description: APIs to retrieve compliance events for regulated members
  name: LinkedIn Compliance Events API
  slug: linkedin-compliance-events-api
- description: 1. Obtain user authorization with consent to create and manage conversions using `rw_conversions`, `r_ads` permissions in the scope. 2. Retrieve authenticated user's sponsored Ad Accounts where user h
  name: LinkedIn Conversion Events Streaming Workflow API
  slug: linkedin-conversion-events-streaming-workflow-api
- description: APIs to create and manage ad creatives
  name: LinkedIn Creative Management API
  slug: linkedin-creative-management-api
- description: Create and manage CRM data validation export jobs
  name: LinkedIn CRM Data Validation API
  slug: linkedin-crm-data-validation-api
- description: APIs for managing customer ATS integrations for premium job posting
  name: LinkedIn Customer Integrations API
  slug: linkedin-customer-integrations-api
- description: Delete synced data from LinkedIn
  name: LinkedIn Data Deletion API
  slug: linkedin-data-deletion-api
- description: Retrieve exported candidates and recruiter interactions
  name: LinkedIn Data Retrieval API
  slug: linkedin-data-retrieval-api
- description: APIs to create and manage DMP segments for audience targeting
  name: LinkedIn DMP Segments API
  slug: linkedin-dmp-segments-api
- description: Events and live video data
  name: LinkedIn Events API
  slug: linkedin-events-api
- description: Posts, reactions, comments, and social metadata
  name: LinkedIn Feed Content API
  slug: linkedin-feed-content-api
- description: Media Planning API can help Media Planners understand the reach and ROI that LinkedIn can offer to their client. It allows them to make budget allocation recommendations with confidence and know how t
  name: LinkedIn Fetch Media Plan API
  slug: linkedin-fetch-media-plan-api
- description: Configure and manage customer ATS integrations
  name: LinkedIn Integration Configuration API
  slug: linkedin-integration-configuration-api
- description: APIs for managing the lifecycle of job postings
  name: LinkedIn Job Lifecycle Management API
  slug: linkedin-job-lifecycle-management-api
- description: Lead generation forms and responses
  name: LinkedIn Lead Generation API
  slug: linkedin-lead-generation-api
- description: APIs to retrieve learning activity reports including completions, views, and logins
  name: LinkedIn Learning Activity Reports API
  slug: linkedin-learning-activity-reports-api
- description: APIs to upload and attach CSV lists to DMP segments
  name: LinkedIn List Uploads API
  slug: linkedin-list-uploads-api
- description: Organization ACLs and authorization data
  name: LinkedIn Organization Access Control API
  slug: linkedin-organization-access-control-api
- description: Organization profile data retrieval
  name: LinkedIn Organizations API
  slug: linkedin-organizations-api
- description: Organizational page content and edge analytics
  name: LinkedIn Page Analytics API
  slug: linkedin-page-analytics-api
- description: Fetch Sales Navigator profile associations from CRM records
  name: LinkedIn Profile Associations API
  slug: linkedin-profile-associations-api
- description: Retrieve sales access tokens for authenticated iframe sessions
  name: LinkedIn Sales Access Tokens API
  slug: linkedin-sales-access-tokens-api
- description: Create and manage sales analytics export jobs
  name: LinkedIn Sales Analytics Export API
  slug: linkedin-sales-analytics-export-api
- description: Manage and retrieve Sales Navigator contracts
  name: LinkedIn Sales Contracts API
  slug: linkedin-sales-contracts-api
- description: This template provides detailed conversion analyses, ideal for in-flight optimization, check-ins, QBRs
  name: LinkedIn Use Cases > B2B Templates > Conversions Deep Dive API
  slug: linkedin-use-cases-b2b-templates-conversions-deep-dive-api
- description: Linkedin is introducing its next generation of APIs to create and manage Conversation Ads, enabling advertisers to better deliver automated messages to a targeted LinkedIn member's inbox. This API rep
  name: LinkedIn Use Cases > Conversation Ad > Sponsored Conversations API
  slug: linkedin-use-cases-conversation-ad-sponsored-conversations-api
- description: Within our API, Conversation Ads are represented by the Sponsored Conversation entity. Sponsored Conversations are composed of Sponsored Message Content.
  name: LinkedIn Use Cases > Conversation Ad > Sponsored Message Contents API
  slug: linkedin-use-cases-conversation-ad-sponsored-message-contents-api
- description: 'The Creatives API contains all the data and information for visually rendering an ad. There are several types of Ad Creatives that you can associate with campaigns including:'
  name: LinkedIn Use Cases > Creatives API
  slug: linkedin-use-cases-creatives-api
- description: The Use Cases > Document Ad API from LinkedIn — 5 operation(s) for use cases > document ad.
  name: LinkedIn Use Cases > Document Ad API
  slug: linkedin-use-cases-document-ad-api
- description: 'Image ads help you engage business decision-makers on LinkedIn''s mobile and desktop news feed. You can create image ads in two ways: \* Post images to your Company Page and sponsor the post to reach m'
  name: LinkedIn Use Cases > Image Ad API
  slug: linkedin-use-cases-image-ad-api
- description: You can set up the message contents sent to targeted LinkedIn members' inbox, either as a Message Ad or a Conversation Ad.
  name: LinkedIn Use Cases > InMail Content API
  slug: linkedin-use-cases-inmail-content-api
- description: The Use Cases > Organization Access Controls API from LinkedIn — 1 operation(s) for use cases > organization access controls.
  name: LinkedIn Use Cases > Organization Access Controls API
  slug: linkedin-use-cases-organization-access-controls-api
- description: The Use Cases > Organization Followers API from LinkedIn — 2 operation(s) for use cases > organization followers.
  name: LinkedIn Use Cases > Organization Followers API
  slug: linkedin-use-cases-organization-followers-api
- description: The Use Cases > Organization Lookup > Organization Brands API from LinkedIn — 4 operation(s) for use cases > organization lookup > organization brands.
  name: LinkedIn Use Cases > Organization Lookup > Organization Brands API
  slug: linkedin-use-cases-organization-lookup-organization-brands-api
- description: The Use Cases > Organization Lookup > Organizations API from LinkedIn — 3 operation(s) for use cases > organization lookup > organizations.
  name: LinkedIn Use Cases > Organization Lookup > Organizations API
  slug: linkedin-use-cases-organization-lookup-organizations-api
- description: The Posts API facilities the creation and retrieval of organic and sponsored posts.
  name: LinkedIn Use Cases > Posts API
  slug: linkedin-use-cases-posts-api
- description: Notifications for the authenticated member’s organizations can be queried using a criteria finder. Notifications are retained and available to pull for 60 days.
  name: LinkedIn Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Pull Workflow API
  slug: linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-pull-workflow-api
- description: Registered webhook URLs will receive notifications from LinkedIn for subscribed events.
  name: LinkedIn Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Push Workflow API
  slug: linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-push-workflow-api
- description: 'In order to support collecting leads for sponsored use cases, a partner app needs to build a UX where a user is able to select the sponsored accounts and forms to collect leads for. ###### Step 1: Obt'
  name: LinkedIn Use Cases > Sponsored API
  slug: linkedin-use-cases-sponsored-api
- description: Spotlight Ads allow you to showcase your product, service, event, content, and more. Upon clicking your Ad, you navigate to the website or landing page of your choice. Learn more about [Spotlight Ads]
  name: LinkedIn Use Cases > Spotlight Ad API
  slug: linkedin-use-cases-spotlight-ad-api
- description: This API describes usage of Organization Follower Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/follow
  name: LinkedIn Use Cases > Statistics APIs > Organization Follower Statistics API
  slug: linkedin-use-cases-statistics-apis-organization-follower-statistics-api
- description: This API describes usage of Organization Page Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/page-stati
  name: LinkedIn Use Cases > Statistics APIs > Organization Page Statistics API
  slug: linkedin-use-cases-statistics-apis-organization-page-statistics-api
- description: This API describes usage of Organization Share Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/share-sta
  name: LinkedIn Use Cases > Statistics APIs > Organization Share Statistics API
  slug: linkedin-use-cases-statistics-apis-organization-share-statistics-api
- description: The Videos API is a new offering from LinkedIn that features the ability to upload a captions file as well as thumbnail video functionality.
  name: LinkedIn Use Cases > Video Ad API
  slug: linkedin-use-cases-video-ad-api
- description: APIs to manage ad account user access and roles
  name: LinkedIn User Access API
  slug: linkedin-user-access-api
- description: APIs to stream user data for contact targeting
  name: LinkedIn User Streaming API
  slug: linkedin-user-streaming-api
arazzos:
- description: Confirm an organization exists and then publish a text share authored by it.
  name: LinkedIn Create an Organization Share
  slug: linkedin-create-organization-share-workflow
- description: Read a post by URN, and when it exists delete it idempotently.
  name: LinkedIn Delete an Organization Post
  slug: linkedin-delete-organization-post-workflow
- description: Pull an organization's posts, then export the reactions and comments on a chosen activity.
  name: LinkedIn Export Post Engagement
  slug: linkedin-export-post-engagement-workflow
- description: Resolve an organization by its vanity URL, then typeahead-search its followers by keyword.
  name: LinkedIn Find Organization and People
  slug: linkedin-find-org-and-people-workflow
- description: Confirm organization access, then list the administered brands under that parent organization.
  name: LinkedIn Organization Access and Brands
  slug: linkedin-org-access-and-brands-workflow
- description: Resolve an organization, then pull time-bound follower statistics for a date range.
  name: LinkedIn Organization Follower Analytics
  slug: linkedin-organization-follower-analytics-workflow
- description: Resolve an organization, then gather its follower count and lifetime page statistics.
  name: LinkedIn Organization Profile Overview
  slug: linkedin-organization-profile-overview-workflow
- description: Resolve an organization, then pull time-bound share statistics for a date range.
  name: LinkedIn Organization Share Analytics
  slug: linkedin-organization-share-analytics-workflow
- description: Create an organization post, then read it back by URN to confirm it published.
  name: LinkedIn Publish and Verify a Post
  slug: linkedin-publish-and-verify-post-workflow
- description: Confirm organization access, then pull pending social action notifications.
  name: LinkedIn Pull Social Action Notifications
  slug: linkedin-pull-social-action-notifications-workflow
- description: Register a webhook subscription for organization social actions, then read it back.
  name: LinkedIn Subscribe to Social Action Notifications
  slug: linkedin-subscribe-social-action-notifications-workflow
- description: Read a post by URN, and when it exists patch its commentary and call to action.
  name: LinkedIn Update an Organization Post
  slug: linkedin-update-organization-post-workflow
- description: Register a document upload, push the file bytes, then publish a document post.
  name: LinkedIn Upload a Document and Create a Post
  slug: linkedin-upload-document-and-create-post-workflow
- description: Register an image upload, confirm the image asset, then publish a post that references it.
  name: LinkedIn Upload an Image and Create a Post
  slug: linkedin-upload-image-and-create-post-workflow
- description: Register a video upload for an owner, then confirm the resulting video asset resolves.
  name: LinkedIn Upload a Video and Verify the Asset
  slug: linkedin-upload-video-and-verify-workflow
artifact_total: 807
collections:
- collection_type: postman
  name: LinkedIn Compliance Events API
  slug: postman-linkedin-compliance-events
- collection_type: postman
  name: LinkedIn Learning Activity Reports API
  slug: postman-linkedin-learning-activity-reports
- collection_type: postman
  name: LinkedIn Marketing Audience Insights API
  slug: postman-linkedin-marketing-audience-insights
- collection_type: postman
  name: LinkedIn Marketing Audiences API
  slug: postman-linkedin-marketing-audience
- collection_type: postman
  name: LinkedIn Marketing Campaign Management API
  slug: postman-linkedin-marketing-campaigns
- collection_type: postman
  name: Community Management
  slug: postman-linkedin-marketing-community
- collection_type: postman
  name: Content APIs
  slug: postman-linkedin-marketing-content
- collection_type: postman
  name: Conversions API
  slug: postman-linkedin-marketing-conversions
- collection_type: postman
  name: Lead Sync
  slug: postman-linkedin-marketing-leads
- collection_type: postman
  name: Media Planning
  slug: postman-linkedin-marketing-media-planning
- collection_type: postman
  name: Reporting & ROI
  slug: postman-linkedin-marketing-reporting-roi
- collection_type: postman
  name: LinkedIn Pages Data Portability API
  slug: postman-linkedin-regulations-data-portability
- collection_type: postman
  name: LinkedIn Ads Transparency API
  slug: postman-linkedin-regulatory-ads-transparency
- collection_type: postman
  name: LinkedIn Sales Navigator API
  slug: postman-linkedin-sales-navigator
- collection_type: postman
  name: LinkedIn Job Posting API
  slug: postman-linkedin-talent-job-posting
- collection_type: postman
  name: LinkedIn Parent Application Management API
  slug: postman-linkedin-talent-learning-parent-application
- collection_type: postman
  name: LinkedIn Recruiter System Connect API
  slug: postman-linkedin-talent-recruiter-system-connect
- collection_type: open
  name: LinkedIn Compliance Events API
  slug: open-linkedin-compliance-events
- collection_type: open
  name: LinkedIn Learning Activity Reports API
  slug: open-linkedin-learning-activity-reports
- collection_type: open
  name: LinkedIn Marketing Audience Insights API
  slug: open-linkedin-marketing-audience-insights
- collection_type: open
  name: LinkedIn Marketing Audiences API
  slug: open-linkedin-marketing-audience
- collection_type: open
  name: LinkedIn Marketing Campaign Management API
  slug: open-linkedin-marketing-campaigns
- collection_type: open
  name: Community Management
  slug: open-linkedin-marketing-community
- collection_type: open
  name: Content APIs
  slug: open-linkedin-marketing-content
- collection_type: open
  name: Conversions API
  slug: open-linkedin-marketing-conversions
- collection_type: open
  name: Lead Sync
  slug: open-linkedin-marketing-leads
- collection_type: open
  name: Media Planning
  slug: open-linkedin-marketing-media-planning
- collection_type: open
  name: Reporting & ROI
  slug: open-linkedin-marketing-reporting-roi
- collection_type: open
  name: LinkedIn Pages Data Portability API
  slug: open-linkedin-regulations-data-portability
- collection_type: open
  name: LinkedIn Ads Transparency API
  slug: open-linkedin-regulatory-ads-transparency
- collection_type: open
  name: LinkedIn Sales Navigator API
  slug: open-linkedin-sales-navigator
- collection_type: open
  name: LinkedIn Job Posting API
  slug: open-linkedin-talent-job-posting
- collection_type: open
  name: LinkedIn Parent Application Management API
  slug: open-linkedin-talent-learning-parent-application
- collection_type: open
  name: LinkedIn Recruiter System Connect API
  slug: open-linkedin-talent-recruiter-system-connect
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/linkedin/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linkedin-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/linkedin-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linkedin-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/linkedin-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linkedin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkedin-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/linkedin-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linkedin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linkedin-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linkedin-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linkedin-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/linkedin-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linkedin-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-compliance-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-learning-activity-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-audience-insights-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-audience-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-community-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-conversions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-leads-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-media-planning-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-reporting-roi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-regulations-data-portability-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-regulatory-ads-transparency-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-sales-navigator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-job-posting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-learning-parent-application-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-recruiter-system-connect-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkedin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkedin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkedin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linkedin-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-create-organization-share-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-delete-organization-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-export-post-engagement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-find-org-and-people-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-org-access-and-brands-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-follower-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-profile-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-share-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-publish-and-verify-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-pull-social-action-notifications-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-subscribe-social-action-notifications-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-update-organization-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-document-and-create-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-image-and-create-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-video-and-verify-workflow.yml
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://www.linkedin.com/oauth/.well-known/openid-configuration
- group: build
  title: ''
  type: CodeExamples
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/sample-applications
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/marketing/versioning
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts?context=linkedin/consumer/context
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin/consumer/context
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/plugins?context=linkedin/consumer/context
- group: start
  title: ''
  type: Portal
  url: https://www.linkedin.com/developers/
- group: start
  title: ''
  type: Signup
  url: https://www.linkedin.com/developers/apps
- group: build
  title: ''
  type: Tools
  url: https://www.linkedin.com/developers/tools/oauth
- group: operate
  title: ''
  type: StatusPage
  url: https://www.linkedin-apistatus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/content/developers/news
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens
- group: build
  title: ''
  type: Tools
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkedin-developers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/linkedin-developers/linkedin-api-js-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/linkedin-developers/linkedin-api-python-client
- group: operate
  title: ''
  type: Support
  url: https://developer.linkedin.com/support
- group: build
  title: ''
  type: Tools
  url: https://github.com/linkedin-developers/linkedin-capi-tag-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/linkedin-developers/java-sample-application
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linkedin.com/legal/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkedin.com/legal/privacy-policy
created: '2024-04-14'
description: LinkedIn is a professional networking platform providing APIs for consumer integrations (Sign In, Share, Verified on LinkedIn), marketing solutions (ad campaigns, audiences, conversions, analytics), talent solutions (job posting, recruiter system connect), learning solutions (activity reports, content), sales navigator (CRM sync, display, analytics), compliance (message archiving), and regulatory data portability.
examples:
- key_count: 6
  name: Linkedin Attachlisttosegment Example
  slug: linkedin-attachlisttosegment-example
- key_count: 6
  name: Linkedin Batchgetprofileassociations Example
  slug: linkedin-batchgetprofileassociations-example
- key_count: 4
  name: Linkedin Compliance Events Compliance Authorization Example
  slug: linkedin-compliance-events-compliance-authorization-example
- key_count: 1
  name: Linkedin Compliance Events Compliance Authorization Request Example
  slug: linkedin-compliance-events-compliance-authorization-request-example
- key_count: 2
  name: Linkedin Compliance Events Compliance Authorization Response Example
  slug: linkedin-compliance-events-compliance-authorization-response-example
- key_count: 10
  name: Linkedin Compliance Events Compliance Event Example
  slug: linkedin-compliance-events-compliance-event-example
- key_count: 2
  name: Linkedin Compliance Events Compliance Events Response Example
  slug: linkedin-compliance-events-compliance-events-response-example
- key_count: 3
  name: Linkedin Compliance Events Error Response Example
  slug: linkedin-compliance-events-error-response-example
- key_count: 3
  name: Linkedin Compliance Events Member Profile Example
  slug: linkedin-compliance-events-member-profile-example
- key_count: 4
  name: Linkedin Compliance Events Paging Example
  slug: linkedin-compliance-events-paging-example
- key_count: 3
  name: Linkedin Compliance Events Paging Link Example
  slug: linkedin-compliance-events-paging-link-example
- key_count: 6
  name: Linkedin Createadaccount Example
  slug: linkedin-createadaccount-example
- key_count: 6
  name: Linkedin Createadaccountuser Example
  slug: linkedin-createadaccountuser-example
- key_count: 6
  name: Linkedin Createcreative Example
  slug: linkedin-createcreative-example
- key_count: 6
  name: Linkedin Createcrmdatavalidationexportjob Example
  slug: linkedin-createcrmdatavalidationexportjob-example
- key_count: 6
  name: Linkedin Createdmpsegment Example
  slug: linkedin-createdmpsegment-example
- key_count: 6
  name: Linkedin Createsalesanalyticsexportjob Example
  slug: linkedin-createsalesanalyticsexportjob-example
- key_count: 6
  name: Linkedin Getadaccountbyid Example
  slug: linkedin-getadaccountbyid-example
- key_count: 6
  name: Linkedin Getadaccountuser Example
  slug: linkedin-getadaccountuser-example
- key_count: 6
  name: Linkedin Getaudiencecount Example
  slug: linkedin-getaudiencecount-example
- key_count: 6
  name: Linkedin Getauthenticateduseradaccounts Example
  slug: linkedin-getauthenticateduseradaccounts-example
- key_count: 6
  name: Linkedin Getcampaignbyid Example
  slug: linkedin-getcampaignbyid-example
- key_count: 6
  name: Linkedin Getcampaigngroupbyid Example
  slug: linkedin-getcampaigngroupbyid-example
- key_count: 6
  name: Linkedin Getdmpsegments Example
  slug: linkedin-getdmpsegments-example
- key_count: 6
  name: Linkedin Getlearningactivityreports Example
  slug: linkedin-getlearningactivityreports-example
- key_count: 6
  name: Linkedin Getorganizationacls Example
  slug: linkedin-getorganizationacls-example
- key_count: 3
  name: Linkedin Learning Activity Reports Error Response Example
  slug: linkedin-learning-activity-reports-error-response-example
- key_count: 1
  name: Linkedin Learning Activity Reports Learner Details Example
  slug: linkedin-learning-activity-reports-learner-details-example
- key_count: 4
  name: Linkedin Learning Activity Reports Learner Entity Example
  slug: linkedin-learning-activity-reports-learner-entity-example
- key_count: 6
  name: Linkedin Learning Activity Reports Learning Activity Example
  slug: linkedin-learning-activity-reports-learning-activity-example
- key_count: 3
  name: Linkedin Learning Activity Reports Learning Activity Report Example
  slug: linkedin-learning-activity-reports-learning-activity-report-example
- key_count: 2
  name: Linkedin Learning Activity Reports Learning Activity Report Response Example
  slug: linkedin-learning-activity-reports-learning-activity-report-response-example
- key_count: 4
  name: Linkedin Learning Activity Reports Paging Example
  slug: linkedin-learning-activity-reports-paging-example
- key_count: 3
  name: Linkedin Learning Activity Reports Paging Link Example
  slug: linkedin-learning-activity-reports-paging-link-example
- key_count: 4
  name: Linkedin Marketing Audience Ad Account Example
  slug: linkedin-marketing-audience-ad-account-example
- key_count: 2
  name: Linkedin Marketing Audience Ad Accounts Response Example
  slug: linkedin-marketing-audience-ad-accounts-response-example
- key_count: 4
  name: Linkedin Marketing Audience Company Stream Element Example
  slug: linkedin-marketing-audience-company-stream-element-example
- key_count: 1
  name: Linkedin Marketing Audience Company Stream Request Example
  slug: linkedin-marketing-audience-company-stream-request-example
- key_count: 6
  name: Linkedin Marketing Audience Dmp Segment Create Request Example
  slug: linkedin-marketing-audience-dmp-segment-create-request-example
- key_count: 10
  name: Linkedin Marketing Audience Dmp Segment Example
  slug: linkedin-marketing-audience-dmp-segment-example
- key_count: 2
  name: Linkedin Marketing Audience Dmp Segments Response Example
  slug: linkedin-marketing-audience-dmp-segments-response-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Ad Targeting Entities Response Example
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Ad Targeting Entity Example
  slug: linkedin-marketing-audience-insights-ad-targeting-entity-example
- key_count: 4
  name: Linkedin Marketing Audience Insights Ad Targeting Facet Example
  slug: linkedin-marketing-audience-insights-ad-targeting-facet-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Ad Targeting Facets Response Example
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Audience Insight Example
  slug: linkedin-marketing-audience-insights-audience-insight-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Audience Insights Request Example
  slug: linkedin-marketing-audience-insights-audience-insights-request-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Audience Insights Response Example
  slug: linkedin-marketing-audience-insights-audience-insights-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Error Response Example
  slug: linkedin-marketing-audience-insights-error-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Insight Segmentation Example
  slug: linkedin-marketing-audience-insights-insight-segmentation-example
- key_count: 4
  name: Linkedin Marketing Audience Insights Paging Example
  slug: linkedin-marketing-audience-insights-paging-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Paging Link Example
  slug: linkedin-marketing-audience-insights-paging-link-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Request Meta Data Example
  slug: linkedin-marketing-audience-insights-request-meta-data-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Targeting Criteria Example
  slug: linkedin-marketing-audience-insights-targeting-criteria-example
- key_count: 1
  name: Linkedin Marketing Audience List Upload Request Example
  slug: linkedin-marketing-audience-list-upload-request-example
- key_count: 4
  name: Linkedin Marketing Audience Paging Example
  slug: linkedin-marketing-audience-paging-example
- key_count: 1
  name: Linkedin Marketing Audience Segment Destination Example
  slug: linkedin-marketing-audience-segment-destination-example
- key_count: 1
  name: Linkedin Marketing Audience Stream Response Example
  slug: linkedin-marketing-audience-stream-response-example
- key_count: 1
  name: Linkedin Marketing Audience Stream Result Element Example
  slug: linkedin-marketing-audience-stream-result-element-example
- key_count: 2
  name: Linkedin Marketing Audience User Id Example
  slug: linkedin-marketing-audience-user-id-example
- key_count: 2
  name: Linkedin Marketing Audience User Stream Element Example
  slug: linkedin-marketing-audience-user-stream-element-example
- key_count: 1
  name: Linkedin Marketing Audience User Stream Request Example
  slug: linkedin-marketing-audience-user-stream-request-example
- key_count: 9
  name: Linkedin Marketing Campaigns Ad Account Create Request Example
  slug: linkedin-marketing-campaigns-ad-account-create-request-example
- key_count: 10
  name: Linkedin Marketing Campaigns Ad Account Example
  slug: linkedin-marketing-campaigns-ad-account-example
- key_count: 3
  name: Linkedin Marketing Campaigns Ad Account User Create Request Example
  slug: linkedin-marketing-campaigns-ad-account-user-create-request-example
- key_count: 3
  name: Linkedin Marketing Campaigns Ad Account User Example
  slug: linkedin-marketing-campaigns-ad-account-user-example
- key_count: 1
  name: Linkedin Marketing Campaigns Ad Account User Update Request Example
  slug: linkedin-marketing-campaigns-ad-account-user-update-request-example
- key_count: 2
  name: Linkedin Marketing Campaigns Audience Count Example
  slug: linkedin-marketing-campaigns-audience-count-example
- key_count: 2
  name: Linkedin Marketing Campaigns Budget Example
  slug: linkedin-marketing-campaigns-budget-example
- key_count: 10
  name: Linkedin Marketing Campaigns Campaign Example
  slug: linkedin-marketing-campaigns-campaign-example
- key_count: 6
  name: Linkedin Marketing Campaigns Campaign Group Example
  slug: linkedin-marketing-campaigns-campaign-group-example
- key_count: 1
  name: Linkedin Marketing Campaigns Campaign Update Request Example
  slug: linkedin-marketing-campaigns-campaign-update-request-example
- key_count: 5
  name: Linkedin Marketing Campaigns Creative Create Request Example
  slug: linkedin-marketing-campaigns-creative-create-request-example
- key_count: 5
  name: Linkedin Marketing Campaigns Creative Example
  slug: linkedin-marketing-campaigns-creative-example
- key_count: 3
  name: Linkedin Marketing Campaigns Organization Acl Example
  slug: linkedin-marketing-campaigns-organization-acl-example
- key_count: 4
  name: Linkedin Marketing Campaigns Paging Example
  slug: linkedin-marketing-campaigns-paging-example
- key_count: 2
  name: Linkedin Marketing Campaigns Run Schedule Example
  slug: linkedin-marketing-campaigns-run-schedule-example
- key_count: 3
  name: Linkedin Marketing Community Batch Get On Administered Response200 Example
  slug: linkedin-marketing-community-batch-get-on-administered-response200-example
- key_count: 3
  name: Linkedin Marketing Community Batch Get On Nonadministered Response200 Example
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200-example
- key_count: 2
  name: Linkedin Marketing Community Find Administered Organization Brands Response200 Example
  slug: linkedin-marketing-community-find-administered-organization-brands-response200-example
- key_count: 3
  name: Linkedin Marketing Community Find Nonadministered Organization Response200 Example
  slug: linkedin-marketing-community-find-nonadministered-organization-response200-example
- key_count: 1
  name: Linkedin Marketing Community Lookup By Organization Primary Response200 Example
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200-example
- key_count: 10
  name: Linkedin Marketing Community Retrieve An Administered Organization Response200 Example
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200-example
- key_count: 1
  name: Linkedin Marketing Community Retrieve Organization Follower Count Response200 Example
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200-example
- key_count: 10
  name: Linkedin Marketing Conversions Create A New Conversion Response201 Example
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201-example
- key_count: 2
  name: Linkedin Marketing Conversions Fetch Active Campaigns Response200 Example
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200-example
- key_count: 2
  name: Linkedin Marketing Conversions Fetch Existing Conversion Rules Response200 Example
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200-example
- key_count: 2
  name: Linkedin Marketing Conversions Retrieve Authenticated Users Sponsored Response200 Example
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200-example
- key_count: 1
  name: Linkedin Marketing Conversions Stream Multiple Conversion Events Response200 Example
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200-example
- key_count: 10
  name: Linkedin Marketing Leads Fetch Full Lead Data Response200 Example
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Get Forms For The Response200 Example
  slug: linkedin-marketing-leads-get-forms-for-the-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Get The Users Sponsored Response200 Example
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Validate The Users Organization Response200 Example
  slug: linkedin-marketing-leads-validate-the-users-organization-response200-example
- key_count: 2
  name: Linkedin Marketing Media Planning Get A List Of Response200 Example
  slug: linkedin-marketing-media-planning-get-a-list-of-response200-example
- key_count: 2
  name: Linkedin Marketing Media Planning Get Bing Geo Locations Response200 Example
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200-example
- key_count: 2
  name: Linkedin Marketing Reporting Roi Conversions By Member Company Response200 Example
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200-example
- key_count: 6
  name: Linkedin Optinmemberforcompliance Example
  slug: linkedin-optinmemberforcompliance-example
- key_count: 5
  name: Linkedin Regulations Data Portability Address Example
  slug: linkedin-regulations-data-portability-address-example
- key_count: 3
  name: Linkedin Regulations Data Portability Batch Organization Response Example
  slug: linkedin-regulations-data-portability-batch-organization-response-example
- key_count: 3
  name: Linkedin Regulations Data Portability Date Info Example
  slug: linkedin-regulations-data-portability-date-info-example
- key_count: 3
  name: Linkedin Regulations Data Portability Image Asset Example
  slug: linkedin-regulations-data-portability-image-asset-example
- key_count: 3
  name: Linkedin Regulations Data Portability Image Reference Example
  slug: linkedin-regulations-data-portability-image-reference-example
- key_count: 2
  name: Linkedin Regulations Data Portability Locale Example
  slug: linkedin-regulations-data-portability-locale-example
- key_count: 2
  name: Linkedin Regulations Data Portability Localized String Example
  slug: linkedin-regulations-data-portability-localized-string-example
- key_count: 5
  name: Linkedin Regulations Data Portability Organization Acl Example
  slug: linkedin-regulations-data-portability-organization-acl-example
- key_count: 2
  name: Linkedin Regulations Data Portability Organization Acl Response Example
  slug: linkedin-regulations-data-portability-organization-acl-response-example
- key_count: 5
  name: Linkedin Regulations Data Portability Organization Location Example
  slug: linkedin-regulations-data-portability-organization-location-example
- key_count: 10
  name: Linkedin Regulations Data Portability Organization Response Example
  slug: linkedin-regulations-data-portability-organization-response-example
- key_count: 7
  name: Linkedin Regulations Data Portability Post Example
  slug: linkedin-regulations-data-portability-post-example
- key_count: 2
  name: Linkedin Regulations Data Portability Post Response Example
  slug: linkedin-regulations-data-portability-post-response-example
- key_count: 2
  name: Linkedin Regulations Data Portability Reaction Response Example
  slug: linkedin-regulations-data-portability-reaction-response-example
- key_count: 1
  name: Linkedin Regulations Data Portability Timestamp Example
  slug: linkedin-regulations-data-portability-timestamp-example
- key_count: 2
  name: Linkedin Regulatory Ads Transparency Advertiser Transparency Request Example
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request-example
- key_count: 7
  name: Linkedin Regulatory Ads Transparency Advertiser Transparency Response Example
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response-example
- key_count: 3
  name: Linkedin Regulatory Ads Transparency Error Response Example
  slug: linkedin-regulatory-ads-transparency-error-response-example
- key_count: 3
  name: Linkedin Sales Navigator Batch Profile Association Response Example
  slug: linkedin-sales-navigator-batch-profile-association-response-example
- key_count: 4
  name: Linkedin Sales Navigator Contract Example
  slug: linkedin-sales-navigator-contract-example
- key_count: 2
  name: Linkedin Sales Navigator Contracts Response Example
  slug: linkedin-sales-navigator-contracts-response-example
- key_count: 7
  name: Linkedin Sales Navigator Crm Data Validation Export Job Example
  slug: linkedin-sales-navigator-crm-data-validation-export-job-example
- key_count: 1
  name: Linkedin Sales Navigator Crm Data Validation Export Job Request Example
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request-example
- key_count: 3
  name: Linkedin Sales Navigator Error Response Example
  slug: linkedin-sales-navigator-error-response-example
- key_count: 3
  name: Linkedin Sales Navigator Paging Example
  slug: linkedin-sales-navigator-paging-example
- key_count: 2
  name: Linkedin Sales Navigator Sales Access Token Example
  slug: linkedin-sales-navigator-sales-access-token-example
- key_count: 2
  name: Linkedin Sales Navigator Sales Access Token Response Example
  slug: linkedin-sales-navigator-sales-access-token-response-example
- key_count: 5
  name: Linkedin Sales Navigator Sales Analytics Export Job Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Analytics Export Job Request Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-request-example
- key_count: 1
  name: Linkedin Sales Navigator Sales Analytics Export Job Response Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-response-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Navigator Profile Association Example
  slug: linkedin-sales-navigator-sales-navigator-profile-association-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Navigator Profile Association Key Example
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key-example
- key_count: 6
  name: Linkedin Searchadaccounts Example
  slug: linkedin-searchadaccounts-example
- key_count: 6
  name: Linkedin Searchcampaigngroups Example
  slug: linkedin-searchcampaigngroups-example
- key_count: 6
  name: Linkedin Searchcampaigns Example
  slug: linkedin-searchcampaigns-example
- key_count: 6
  name: Linkedin Streamcompaniestosegment Example
  slug: linkedin-streamcompaniestosegment-example
- key_count: 1
  name: Linkedin Talent Job Posting Additional Questions Example
  slug: linkedin-talent-job-posting-additional-questions-example
- key_count: 6
  name: Linkedin Talent Job Posting Application Questions Example
  slug: linkedin-talent-job-posting-application-questions-example
- key_count: 1
  name: Linkedin Talent Job Posting Cover Letter Questions Example
  slug: linkedin-talent-job-posting-cover-letter-questions-example
- key_count: 4
  name: Linkedin Talent Job Posting Custom Question Example
  slug: linkedin-talent-job-posting-custom-question-example
- key_count: 2
  name: Linkedin Talent Job Posting Custom Question Set Example
  slug: linkedin-talent-job-posting-custom-question-set-example
- key_count: 1
  name: Linkedin Talent Job Posting Education Questions Example
  slug: linkedin-talent-job-posting-education-questions-example
- key_count: 10
  name: Linkedin Talent Job Posting Job Posting Element Example
  slug: linkedin-talent-job-posting-job-posting-element-example
- key_count: 1
  name: Linkedin Talent Job Posting Job Posting Response Example
  slug: linkedin-talent-job-posting-job-posting-response-example
- key_count: 3
  name: Linkedin Talent Job Posting Multiple Choice Question Details Example
  slug: linkedin-talent-job-posting-multiple-choice-question-details-example
- key_count: 2
  name: Linkedin Talent Job Posting Onsite Apply Configuration Example
  slug: linkedin-talent-job-posting-onsite-apply-configuration-example
- key_count: 2
  name: Linkedin Talent Job Posting Question Choice Example
  slug: linkedin-talent-job-posting-question-choice-example
- key_count: 1
  name: Linkedin Talent Job Posting Question Details Example
  slug: linkedin-talent-job-posting-question-details-example
- key_count: 1
  name: Linkedin Talent Job Posting Resume Questions Example
  slug: linkedin-talent-job-posting-resume-questions-example
- key_count: 1
  name: Linkedin Talent Job Posting Simple Job Posting Request Example
  slug: linkedin-talent-job-posting-simple-job-posting-request-example
- key_count: 1
  name: Linkedin Talent Job Posting Work Questions Example
  slug: linkedin-talent-job-posting-work-questions-example
- key_count: 4
  name: Linkedin Talent Learning Parent Application Application Credentials Example
  slug: linkedin-talent-learning-parent-application-application-credentials-example
- key_count: 3
  name: Linkedin Talent Learning Parent Application Error Response Example
  slug: linkedin-talent-learning-parent-application-error-response-example
- key_count: 1
  name: Linkedin Talent Learning Parent Application Get Application Response Example
  slug: linkedin-talent-learning-parent-application-get-application-response-example
- key_count: 5
  name: Linkedin Talent Learning Parent Application Provision Application Request Example
  slug: linkedin-talent-learning-parent-application-provision-application-request-example
- key_count: 8
  name: Linkedin Talent Learning Parent Application Provision Application Response Example
  slug: linkedin-talent-learning-parent-application-provision-application-response-example
- key_count: 1
  name: Linkedin Talent Learning Parent Application Update Callback Url Request Example
  slug: linkedin-talent-learning-parent-application-update-callback-url-request-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Access Token Request Example
  slug: linkedin-talent-recruiter-system-connect-access-token-request-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Access Token Response Example
  slug: linkedin-talent-recruiter-system-connect-access-token-response-example
- key_count: 6
  name: Linkedin Talent Recruiter System Connect Address Example
  slug: linkedin-talent-recruiter-system-connect-address-example
- key_count: 10
  name: Linkedin Talent Recruiter System Connect Application Data Example
  slug: linkedin-talent-recruiter-system-connect-application-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Application Request Example
  slug: linkedin-talent-recruiter-system-connect-application-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Ats Integration Update Request Example
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request-example
- key_count: 10
  name: Linkedin Talent Recruiter System Connect Candidate Data Example
  slug: linkedin-talent-recruiter-system-connect-candidate-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Candidate Request Example
  slug: linkedin-talent-recruiter-system-connect-candidate-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Configuration Value Example
  slug: linkedin-talent-recruiter-system-connect-configuration-value-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Integration Configuration Request Example
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Integration Patch Example
  slug: linkedin-talent-recruiter-system-connect-integration-patch-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Note Data Example
  slug: linkedin-talent-recruiter-system-connect-note-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Note Request Example
  slug: linkedin-talent-recruiter-system-connect-note-request-example
- key_count: 2
  name: Linkedin Talent Recruiter System Connect Person Name Example
  slug: linkedin-talent-recruiter-system-connect-person-name-example
- key_count: 2
  name: Linkedin Talent Recruiter System Connect Phone Number Example
  slug: linkedin-talent-recruiter-system-connect-phone-number-example
- key_count: 6
  name: Linkedin Updateadaccount Example
  slug: linkedin-updateadaccount-example
features:
- description: OpenID Connect-based authentication enabling users to sign in to third-party applications with their LinkedIn credentials.
  name: Sign In with LinkedIn
- description: Enable users to share content from your application directly to their LinkedIn feed.
  name: Share on LinkedIn
- description: Display verified professional credentials and certifications from LinkedIn on third-party platforms.
  name: Verified on LinkedIn
- description: Programmatically create, manage, and optimize B2B advertising campaigns with targeting and budget controls.
  name: Campaign Management
- description: Access aggregated audience demographics and firmographic data for ad targeting and market research.
  name: Audience Insights
- description: Send online and offline conversion events for attribution and campaign optimization.
  name: Conversions API
- description: Collect leads directly from LinkedIn ads with pre-filled forms using member profile data.
  name: Lead Gen Forms
- description: Programmatically publish and manage job listings on LinkedIn through the Talent Solutions API.
  name: Job Posting
- description: Integrate applicant tracking systems with LinkedIn Recruiter for seamless candidate management.
  name: Recruiter System Connect
- description: Retrieve learner engagement, completions, and activity data from LinkedIn Learning.
  name: Learning Activity Reports
- description: Archive and monitor LinkedIn messages and activities for regulatory compliance in regulated industries.
  name: Compliance Archiving
- description: Access member and organization data portability endpoints for Digital Markets Act compliance.
  name: Data Portability
finops:
- name: Linkedin Finops
  service_category: Marketing / Recruiting / Professional Networking
  slug: linkedin-finops
graphqls:
- description: LinkedIn does not expose a native public GraphQL API. All LinkedIn developer APIs are REST-based, documented at [https://learn.microsoft.com/en-us/linkedin/](https://learn.microsoft.com/en-us/linkedin
  name: LinkedIn GraphQL Schema
  slug: linkedin-graphql
image: https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg
integrations:
- description: LinkedIn Sales Navigator integration with Salesforce CRM for lead and account synchronization.
  name: Salesforce
- description: Native integration with Microsoft Dynamics 365 for sales intelligence and lead management.
  name: Microsoft Dynamics
- description: LinkedIn Ads integration with HubSpot for campaign management and lead synchronization.
  name: HubSpot
- description: Official Postman workspaces for all LinkedIn API business lines with pre-built collections.
  name: Postman
- description: Standards-based authentication using OpenID Connect for Sign In with LinkedIn.
  name: OpenID Connect
json_schemas:
- name: AccessTokenRequest
  property_count: 3
  slug: linkedin-accesstokenrequest
- name: AccessTokenResponse
  property_count: 3
  slug: linkedin-accesstokenresponse
- name: AdAccount
  property_count: 4
  slug: linkedin-adaccount
- name: AdAccountCreateRequest
  property_count: 9
  slug: linkedin-adaccountcreaterequest
- name: AdAccountsResponse
  property_count: 2
  slug: linkedin-adaccountsresponse
- name: AdAccountUser
  property_count: 3
  slug: linkedin-adaccountuser
- name: AdAccountUserCreateRequest
  property_count: 3
  slug: linkedin-adaccountusercreaterequest
- name: AdAccountUserUpdateRequest
  property_count: 1
  slug: linkedin-adaccountuserupdaterequest
- name: AdditionalQuestions
  property_count: 1
  slug: linkedin-additionalquestions
- name: Address
  property_count: 5
  slug: linkedin-address
- name: AdTargetingEntitiesResponse
  property_count: 2
  slug: linkedin-adtargetingentitiesresponse
- name: AdTargetingEntity
  property_count: 3
  slug: linkedin-adtargetingentity
- name: AdTargetingFacet
  property_count: 4
  slug: linkedin-adtargetingfacet
- name: AdTargetingFacetsResponse
  property_count: 2
  slug: linkedin-adtargetingfacetsresponse
- name: AdvertiserTransparencyRequest
  property_count: 2
  slug: linkedin-advertisertransparencyrequest
- name: AdvertiserTransparencyResponse
  property_count: 7
  slug: linkedin-advertisertransparencyresponse
- name: AnalyticsRecord
  property_count: 7
  slug: linkedin-analyticsrecord
- name: AnalyticsResponse
  property_count: 2
  slug: linkedin-analyticsresponse
- name: ApplicationCredentials
  property_count: 4
  slug: linkedin-applicationcredentials
- name: ApplicationData
  property_count: 10
  slug: linkedin-applicationdata
- name: ApplicationQuestions
  property_count: 6
  slug: linkedin-applicationquestions
- name: ApplicationRequest
  property_count: 1
  slug: linkedin-applicationrequest
- name: AssociateCampaignsToConversionRequest
  property_count: 0
  slug: linkedin-associatecampaignstoconversionrequest
- name: AssociateCampaignsToConversionResponse204
  property_count: 0
  slug: linkedin-associatecampaignstoconversionresponse204
- name: AtsIntegrationDetail
  property_count: 4
  slug: linkedin-atsintegrationdetail
- name: AtsIntegrationPatch
  property_count: 1
  slug: linkedin-atsintegrationpatch
- name: AtsIntegrationResponse
  property_count: 1
  slug: linkedin-atsintegrationresponse
- name: AtsIntegrationUpdateRequest
  property_count: 1
  slug: linkedin-atsintegrationupdaterequest
- name: AudienceCount
  property_count: 2
  slug: linkedin-audiencecount
- name: AudienceInsight
  property_count: 2
  slug: linkedin-audienceinsight
- name: AudienceInsightsRequest
  property_count: 1
  slug: linkedin-audienceinsightsrequest
- name: AudienceInsightsResponse
  property_count: 1
  slug: linkedin-audienceinsightsresponse
- name: BatchCreateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batchcreatesponsoredmessagerequest
- name: BatchGetOnAdministeredResponse200
  property_count: 3
  slug: linkedin-batchgetonadministeredresponse200
- name: BatchGetOnNonadministeredResponse200
  property_count: 3
  slug: linkedin-batchgetonnonadministeredresponse200
- name: BatchOrganizationResponse
  property_count: 3
  slug: linkedin-batchorganizationresponse
- name: BatchProfileAssociationResponse
  property_count: 3
  slug: linkedin-batchprofileassociationresponse
- name: BatchUpdateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batchupdatesponsoredmessagerequest
- name: Budget
  property_count: 2
  slug: linkedin-budget
- name: Campaign
  property_count: 10
  slug: linkedin-campaign
- name: CampaignGroup
  property_count: 6
  slug: linkedin-campaigngroup
- name: CampaignUpdateRequest
  property_count: 1
  slug: linkedin-campaignupdaterequest
- name: CandidateData
  property_count: 13
  slug: linkedin-candidatedata
- name: CandidateRequest
  property_count: 1
  slug: linkedin-candidaterequest
- name: Comment
  property_count: 5
  slug: linkedin-comment
- name: CommentResponse
  property_count: 2
  slug: linkedin-commentresponse
- name: CompanyStreamElement
  property_count: 4
  slug: linkedin-companystreamelement
- name: CompanyStreamRequest
  property_count: 1
  slug: linkedin-companystreamrequest
- name: ComplianceAuthorizationRequest
  property_count: 1
  slug: linkedin-compliance-events-compliance-authorization-request
- name: ComplianceAuthorizationResponse
  property_count: 2
  slug: linkedin-compliance-events-compliance-authorization-response
- name: ComplianceAuthorization
  property_count: 4
  slug: linkedin-compliance-events-compliance-authorization
- name: ComplianceEvent
  property_count: 15
  slug: linkedin-compliance-events-compliance-event
- name: ComplianceEventsResponse
  property_count: 2
  slug: linkedin-compliance-events-compliance-events-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-compliance-events-error-response
- name: MemberProfile
  property_count: 3
  slug: linkedin-compliance-events-member-profile
- name: PagingLink
  property_count: 3
  slug: linkedin-compliance-events-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-compliance-events-paging
- name: ComplianceAuthorization
  property_count: 4
  slug: linkedin-complianceauthorization
- name: ComplianceAuthorizationRequest
  property_count: 1
  slug: linkedin-complianceauthorizationrequest
- name: ComplianceAuthorizationResponse
  property_count: 2
  slug: linkedin-complianceauthorizationresponse
- name: ComplianceEvent
  property_count: 15
  slug: linkedin-complianceevent
- name: ComplianceEventsResponse
  property_count: 2
  slug: linkedin-complianceeventsresponse
- name: ConfigurationValue
  property_count: 1
  slug: linkedin-configurationvalue
- name: Contract
  property_count: 4
  slug: linkedin-contract
- name: ContractsResponse
  property_count: 2
  slug: linkedin-contractsresponse
- name: ConversionsByMemberCompanyResponse200
  property_count: 2
  slug: linkedin-conversionsbymembercompanyresponse200
- name: CoverLetterQuestions
  property_count: 1
  slug: linkedin-coverletterquestions
- name: CreateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-createadynamicspotlightrequest
- name: CreateANewConversionRequest
  property_count: 0
  slug: linkedin-createanewconversionrequest
- name: CreateANewConversionResponse201
  property_count: 14
  slug: linkedin-createanewconversionresponse201
- name: CreateAShareWithRequest
  property_count: 0
  slug: linkedin-createasharewithrequest
- name: CreateASubscriptionRequestRequest
  property_count: 0
  slug: linkedin-createasubscriptionrequestrequest
- name: CreateDocumentContentRequest
  property_count: 0
  slug: linkedin-createdocumentcontentrequest
- name: CreateInmailContentRequest
  property_count: 0
  slug: linkedin-createinmailcontentrequest
- name: Creative
  property_count: 5
  slug: linkedin-creative
- name: CreativeCreateRequest
  property_count: 5
  slug: linkedin-creativecreaterequest
- name: CrmDataValidationExportJob
  property_count: 7
  slug: linkedin-crmdatavalidationexportjob
- name: CrmDataValidationExportJobRequest
  property_count: 1
  slug: linkedin-crmdatavalidationexportjobrequest
- name: CustomQuestion
  property_count: 4
  slug: linkedin-customquestion
- name: CustomQuestionSet
  property_count: 2
  slug: linkedin-customquestionset
- name: DateInfo
  property_count: 3
  slug: linkedin-dateinfo
- name: DmpSegment
  property_count: 11
  slug: linkedin-dmpsegment
- name: DmpSegmentCreateRequest
  property_count: 6
  slug: linkedin-dmpsegmentcreaterequest
- name: DmpSegmentsResponse
  property_count: 2
  slug: linkedin-dmpsegmentsresponse
- name: EducationQuestions
  property_count: 1
  slug: linkedin-educationquestions
- name: EntityAclRequest
  property_count: 1
  slug: linkedin-entityaclrequest
- name: ErrorDetail
  property_count: 3
  slug: linkedin-errordetail
- name: ErrorResponse
  property_count: 3
  slug: linkedin-errorresponse
- name: Evaluation
  property_count: 2
  slug: linkedin-evaluation
- name: Event
  property_count: 8
  slug: linkedin-event
- name: EventResponse
  property_count: 2
  slug: linkedin-eventresponse
- name: ExportedCandidate
  property_count: 5
  slug: linkedin-exportedcandidate
- name: ExportedCandidateResponse
  property_count: 1
  slug: linkedin-exportedcandidateresponse
- name: FetchActiveCampaignsResponse200
  property_count: 2
  slug: linkedin-fetchactivecampaignsresponse200
- name: FetchExistingConversionRulesResponse200
  property_count: 2
  slug: linkedin-fetchexistingconversionrulesresponse200
- name: FetchFullLeadDataResponse200
  property_count: 10
  slug: linkedin-fetchfullleaddataresponse200
- name: FindAdministeredOrganizationBrandsResponse200
  property_count: 2
  slug: linkedin-findadministeredorganizationbrandsresponse200
- name: FindNonadministeredOrganizationResponse200
  property_count: 3
  slug: linkedin-findnonadministeredorganizationresponse200
- name: ForecastAvgLifetimeFrequencyRequest
  property_count: 0
  slug: linkedin-forecastavglifetimefrequencyrequest
- name: ForecastAvgLifetimeFrequencyResponseundefined
  property_count: 0
  slug: linkedin-forecastavglifetimefrequencyresponseundefined
- name: GetAListOfResponse200
  property_count: 2
  slug: linkedin-getalistofresponse200
- name: GetApplicationResponse
  property_count: 1
  slug: linkedin-getapplicationresponse
- name: GetBingGeoLocationsResponse200
  property_count: 2
  slug: linkedin-getbinggeolocationsresponse200
- name: GetFormsForTheResponse200
  property_count: 2
  slug: linkedin-getformsfortheresponse200
- name: GetTheUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-gettheuserssponsoredresponse200
- name: ImageAsset
  property_count: 3
  slug: linkedin-imageasset
- name: ImageReference
  property_count: 3
  slug: linkedin-imagereference
- name: InitializeImageUploadRequest
  property_count: 0
  slug: linkedin-initializeimageuploadrequest
- name: InitializeVideoUploadRequest
  property_count: 0
  slug: linkedin-initializevideouploadrequest
- name: InsightSegmentation
  property_count: 3
  slug: linkedin-insightsegmentation
- name: IntegrationConfigurationRequest
  property_count: 1
  slug: linkedin-integrationconfigurationrequest
- name: IntegrationPatch
  property_count: 1
  slug: linkedin-integrationpatch
- name: InterviewFeedbackData
  property_count: 4
  slug: linkedin-interviewfeedbackdata
- name: InterviewFeedbackRequest
  property_count: 1
  slug: linkedin-interviewfeedbackrequest
- name: JobPostingElement
  property_count: 10
  slug: linkedin-jobpostingelement
- name: JobPostingResponse
  property_count: 1
  slug: linkedin-jobpostingresponse
- name: JobPostingResult
  property_count: 2
  slug: linkedin-jobpostingresult
- name: JobPostingTaskResponse
  property_count: 1
  slug: linkedin-jobpostingtaskresponse
- name: JobPostingTaskResult
  property_count: 3
  slug: linkedin-jobpostingtaskresult
- name: LeadGenAnswer
  property_count: 2
  slug: linkedin-leadgenanswer
- name: LeadGenRecord
  property_count: 4
  slug: linkedin-leadgenrecord
- name: LeadGenResponse
  property_count: 2
  slug: linkedin-leadgenresponse
- name: LearnerDetails
  property_count: 1
  slug: linkedin-learnerdetails
- name: LearnerEntity
  property_count: 4
  slug: linkedin-learnerentity
- name: ErrorResponse
  property_count: 3
  slug: linkedin-learning-activity-reports-error-response
- name: LearnerDetails
  property_count: 1
  slug: linkedin-learning-activity-reports-learner-details
- name: LearnerEntity
  property_count: 4
  slug: linkedin-learning-activity-reports-learner-entity
- name: LearningActivityReportResponse
  property_count: 2
  slug: linkedin-learning-activity-reports-learning-activity-report-response
- name: LearningActivityReport
  property_count: 3
  slug: linkedin-learning-activity-reports-learning-activity-report
- name: LearningActivity
  property_count: 6
  slug: linkedin-learning-activity-reports-learning-activity
- name: PagingLink
  property_count: 3
  slug: linkedin-learning-activity-reports-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-learning-activity-reports-paging
- name: LearningActivity
  property_count: 6
  slug: linkedin-learningactivity
- name: LearningActivityReport
  property_count: 3
  slug: linkedin-learningactivityreport
- name: LearningActivityReportResponse
  property_count: 2
  slug: linkedin-learningactivityreportresponse
- name: ListUploadRequest
  property_count: 1
  slug: linkedin-listuploadrequest
- name: Locale
  property_count: 2
  slug: linkedin-locale
- name: LocalizedString
  property_count: 2
  slug: linkedin-localizedstring
- name: LookupByOrganizationPrimaryResponse200
  property_count: 1
  slug: linkedin-lookupbyorganizationprimaryresponse200
- name: AdAccount
  property_count: 4
  slug: linkedin-marketing-audience-ad-account
- name: AdAccountsResponse
  property_count: 2
  slug: linkedin-marketing-audience-ad-accounts-response
- name: CompanyStreamElement
  property_count: 4
  slug: linkedin-marketing-audience-company-stream-element
- name: CompanyStreamRequest
  property_count: 1
  slug: linkedin-marketing-audience-company-stream-request
- name: DmpSegmentCreateRequest
  property_count: 6
  slug: linkedin-marketing-audience-dmp-segment-create-request
- name: DmpSegment
  property_count: 11
  slug: linkedin-marketing-audience-dmp-segment
- name: DmpSegmentsResponse
  property_count: 2
  slug: linkedin-marketing-audience-dmp-segments-response
- name: AdTargetingEntitiesResponse
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response
- name: AdTargetingEntity
  property_count: 3
  slug: linkedin-marketing-audience-insights-ad-targeting-entity
- name: AdTargetingFacet
  property_count: 4
  slug: linkedin-marketing-audience-insights-ad-targeting-facet
- name: AdTargetingFacetsResponse
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response
- name: AudienceInsight
  property_count: 2
  slug: linkedin-marketing-audience-insights-audience-insight
- name: AudienceInsightsRequest
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-request
- name: AudienceInsightsResponse
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-marketing-audience-insights-error-response
- name: InsightSegmentation
  property_count: 3
  slug: linkedin-marketing-audience-insights-insight-segmentation
- name: PagingLink
  property_count: 3
  slug: linkedin-marketing-audience-insights-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-marketing-audience-insights-paging
- name: RequestMetaData
  property_count: 1
  slug: linkedin-marketing-audience-insights-request-meta-data
- name: TargetingCriteria
  property_count: 1
  slug: linkedin-marketing-audience-insights-targeting-criteria
- name: ListUploadRequest
  property_count: 1
  slug: linkedin-marketing-audience-list-upload-request
- name: Paging
  property_count: 4
  slug: linkedin-marketing-audience-paging
- name: SegmentDestination
  property_count: 1
  slug: linkedin-marketing-audience-segment-destination
- name: StreamResponse
  property_count: 1
  slug: linkedin-marketing-audience-stream-response
- name: StreamResultElement
  property_count: 1
  slug: linkedin-marketing-audience-stream-result-element
- name: UserId
  property_count: 2
  slug: linkedin-marketing-audience-user-id
- name: UserStreamElement
  property_count: 2
  slug: linkedin-marketing-audience-user-stream-element
- name: UserStreamRequest
  property_count: 1
  slug: linkedin-marketing-audience-user-stream-request
- name: AdAccountCreateRequest
  property_count: 9
  slug: linkedin-marketing-campaigns-ad-account-create-request
- name: AdAccount
  property_count: 11
  slug: linkedin-marketing-campaigns-ad-account
- name: AdAccountUserCreateRequest
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-create-request
- name: AdAccountUser
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user
- name: AdAccountUserUpdateRequest
  property_count: 1
  slug: linkedin-marketing-campaigns-ad-account-user-update-request
- name: AudienceCount
  property_count: 2
  slug: linkedin-marketing-campaigns-audience-count
- name: Budget
  property_count: 2
  slug: linkedin-marketing-campaigns-budget
- name: CampaignGroup
  property_count: 6
  slug: linkedin-marketing-campaigns-campaign-group
- name: Campaign
  property_count: 10
  slug: linkedin-marketing-campaigns-campaign
- name: CampaignUpdateRequest
  property_count: 1
  slug: linkedin-marketing-campaigns-campaign-update-request
- name: CreativeCreateRequest
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-create-request
- name: Creative
  property_count: 5
  slug: linkedin-marketing-campaigns-creative
- name: OrganizationAcl
  property_count: 3
  slug: linkedin-marketing-campaigns-organization-acl
- name: Paging
  property_count: 4
  slug: linkedin-marketing-campaigns-paging
- name: RunSchedule
  property_count: 2
  slug: linkedin-marketing-campaigns-run-schedule
- name: BatchGetOnAdministeredResponse200
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-administered-response200
- name: BatchGetOnNonadministeredResponse200
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200
- name: FindAdministeredOrganizationBrandsResponse200
  property_count: 2
  slug: linkedin-marketing-community-find-administered-organization-brands-response200
- name: FindNonadministeredOrganizationResponse200
  property_count: 3
  slug: linkedin-marketing-community-find-nonadministered-organization-response200
- name: LookupByOrganizationPrimaryResponse200
  property_count: 1
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200
- name: RetrieveAnAdministeredOrganizationResponse200
  property_count: 16
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200
- name: RetrieveOrganizationFollowerCountResponse200
  property_count: 1
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200
- name: CreateANewConversionResponse201
  property_count: 14
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201
- name: FetchActiveCampaignsResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200
- name: FetchExistingConversionRulesResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200
- name: RetrieveAuthenticatedUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200
- name: StreamMultipleConversionEventsResponse200
  property_count: 1
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200
- name: FetchFullLeadDataResponse200
  property_count: 10
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200
- name: GetFormsForTheResponse200
  property_count: 2
  slug: linkedin-marketing-leads-get-forms-for-the-response200
- name: GetTheUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200
- name: ValidateTheUsersOrganizationResponse200
  property_count: 2
  slug: linkedin-marketing-leads-validate-the-users-organization-response200
- name: GetAListOfResponse200
  property_count: 2
  slug: linkedin-marketing-media-planning-get-a-list-of-response200
- name: GetBingGeoLocationsResponse200
  property_count: 2
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200
- name: ConversionsByMemberCompanyResponse200
  property_count: 2
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200
- name: MemberProfile
  property_count: 3
  slug: linkedin-memberprofile
- name: MultipleChoiceQuestionDetails
  property_count: 3
  slug: linkedin-multiplechoicequestiondetails
- name: NoteData
  property_count: 3
  slug: linkedin-notedata
- name: NoteRequest
  property_count: 1
  slug: linkedin-noterequest
- name: OnsiteApplyConfiguration
  property_count: 2
  slug: linkedin-onsiteapplyconfiguration
- name: OrganizationAcl
  property_count: 3
  slug: linkedin-organizationacl
- name: OrganizationAclResponse
  property_count: 2
  slug: linkedin-organizationaclresponse
- name: OrganizationLocation
  property_count: 5
  slug: linkedin-organizationlocation
- name: OrganizationResponse
  property_count: 18
  slug: linkedin-organizationresponse
- name: Paging
  property_count: 4
  slug: linkedin-paging
- name: PagingLink
  property_count: 3
  slug: linkedin-paginglink
- name: PersonName
  property_count: 2
  slug: linkedin-personname
- name: PhoneNumber
  property_count: 2
  slug: linkedin-phonenumber
- name: Post
  property_count: 7
  slug: linkedin-post
- name: PostResponse
  property_count: 2
  slug: linkedin-postresponse
- name: ProvisionApplicationRequest
  property_count: 5
  slug: linkedin-provisionapplicationrequest
- name: ProvisionApplicationResponse
  property_count: 8
  slug: linkedin-provisionapplicationresponse
- name: QuestionChoice
  property_count: 2
  slug: linkedin-questionchoice
- name: QuestionDetails
  property_count: 1
  slug: linkedin-questiondetails
- name: Reaction
  property_count: 3
  slug: linkedin-reaction
- name: ReactionResponse
  property_count: 2
  slug: linkedin-reactionresponse
- name: Address
  property_count: 5
  slug: linkedin-regulations-data-portability-address
- name: BatchOrganizationResponse
  property_count: 3
  slug: linkedin-regulations-data-portability-batch-organization-response
- name: DateInfo
  property_count: 3
  slug: linkedin-regulations-data-portability-date-info
- name: ImageAsset
  property_count: 3
  slug: linkedin-regulations-data-portability-image-asset
- name: ImageReference
  property_count: 3
  slug: linkedin-regulations-data-portability-image-reference
- name: Locale
  property_count: 2
  slug: linkedin-regulations-data-portability-locale
- name: LocalizedString
  property_count: 2
  slug: linkedin-regulations-data-portability-localized-string
- name: OrganizationAclResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-organization-acl-response
- name: OrganizationAcl
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-acl
- name: OrganizationLocation
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-location
- name: OrganizationResponse
  property_count: 18
  slug: linkedin-regulations-data-portability-organization-response
- name: PostResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-post-response
- name: Post
  property_count: 7
  slug: linkedin-regulations-data-portability-post
- name: ReactionResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-reaction-response
- name: Timestamp
  property_count: 1
  slug: linkedin-regulations-data-portability-timestamp
- name: AdvertiserTransparencyRequest
  property_count: 2
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request
- name: AdvertiserTransparencyResponse
  property_count: 7
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-regulatory-ads-transparency-error-response
- name: RequestMetaData
  property_count: 1
  slug: linkedin-requestmetadata
- name: ResumeQuestions
  property_count: 1
  slug: linkedin-resumequestions
- name: ResumeUploadRequest
  property_count: 5
  slug: linkedin-resumeuploadrequest
- name: ResumeUploadResponse
  property_count: 2
  slug: linkedin-resumeuploadresponse
- name: RetrieveAnAdministeredOrganizationResponse200
  property_count: 16
  slug: linkedin-retrieveanadministeredorganizationresponse200
- name: RetrieveAuthenticatedUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-retrieveauthenticateduserssponsoredresponse200
- name: RetrieveOrganizationFollowerCountResponse200
  property_count: 1
  slug: linkedin-retrieveorganizationfollowercountresponse200
- name: RunSchedule
  property_count: 2
  slug: linkedin-runschedule
- name: BatchProfileAssociationResponse
  property_count: 3
  slug: linkedin-sales-navigator-batch-profile-association-response
- name: Contract
  property_count: 4
  slug: linkedin-sales-navigator-contract
- name: ContractsResponse
  property_count: 2
  slug: linkedin-sales-navigator-contracts-response
- name: CrmDataValidationExportJobRequest
  property_count: 1
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request
- name: CrmDataValidationExportJob
  property_count: 7
  slug: linkedin-sales-navigator-crm-data-validation-export-job
- name: ErrorResponse
  property_count: 3
  slug: linkedin-sales-navigator-error-response
- name: Paging
  property_count: 3
  slug: linkedin-sales-navigator-paging
- name: SalesAccessTokenResponse
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-response
- name: SalesAccessToken
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token
- name: SalesAnalyticsExportJobRequest
  property_count: 3
  slug: linkedin-sales-navigator-sales-analytics-export-job-request
- name: SalesAnalyticsExportJobResponse
  property_count: 1
  slug: linkedin-sales-navigator-sales-analytics-export-job-response
- name: SalesAnalyticsExportJob
  property_count: 5
  slug: linkedin-sales-navigator-sales-analytics-export-job
- name: SalesNavigatorProfileAssociationKey
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key
- name: SalesNavigatorProfileAssociation
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association
- name: SalesAccessToken
  property_count: 2
  slug: linkedin-salesaccesstoken
- name: SalesAccessTokenResponse
  property_count: 2
  slug: linkedin-salesaccesstokenresponse
- name: SalesAnalyticsExportJob
  property_count: 5
  slug: linkedin-salesanalyticsexportjob
- name: SalesAnalyticsExportJobRequest
  property_count: 3
  slug: linkedin-salesanalyticsexportjobrequest
- name: SalesAnalyticsExportJobResponse
  property_count: 1
  slug: linkedin-salesanalyticsexportjobresponse
- name: SalesNavigatorProfileAssociation
  property_count: 3
  slug: linkedin-salesnavigatorprofileassociation
- name: SalesNavigatorProfileAssociationKey
  property_count: 3
  slug: linkedin-salesnavigatorprofileassociationkey
- name: Seatholder
  property_count: 5
  slug: linkedin-seatholder
- name: SeatholdersResponse
  property_count: 2
  slug: linkedin-seatholdersresponse
- name: SegmentDestination
  property_count: 1
  slug: linkedin-segmentdestination
- name: SimpleJobPostingRequest
  property_count: 1
  slug: linkedin-simplejobpostingrequest
- name: StageData
  property_count: 2
  slug: linkedin-stagedata
- name: StageRequest
  property_count: 1
  slug: linkedin-stagerequest
- name: StreamMultipleConversionEventsRequest
  property_count: 0
  slug: linkedin-streammultipleconversioneventsrequest
- name: StreamMultipleConversionEventsResponse200
  property_count: 1
  slug: linkedin-streammultipleconversioneventsresponse200
- name: StreamResponse
  property_count: 1
  slug: linkedin-streamresponse
- name: StreamResultElement
  property_count: 1
  slug: linkedin-streamresultelement
- name: SubscribeForLeadNotificationRequest
  property_count: 0
  slug: linkedin-subscribeforleadnotificationrequest
- name: SuccessResponse
  property_count: 1
  slug: linkedin-successresponse
- name: AdditionalQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-additional-questions
- name: ApplicationQuestions
  property_count: 6
  slug: linkedin-talent-job-posting-application-questions
- name: CoverLetterQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-cover-letter-questions
- name: CustomQuestion
  property_count: 4
  slug: linkedin-talent-job-posting-custom-question
- name: CustomQuestionSet
  property_count: 2
  slug: linkedin-talent-job-posting-custom-question-set
- name: EducationQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-education-questions
- name: JobPostingElement
  property_count: 10
  slug: linkedin-talent-job-posting-job-posting-element
- name: JobPostingResponse
  property_count: 1
  slug: linkedin-talent-job-posting-job-posting-response
- name: MultipleChoiceQuestionDetails
  property_count: 3
  slug: linkedin-talent-job-posting-multiple-choice-question-details
- name: OnsiteApplyConfiguration
  property_count: 2
  slug: linkedin-talent-job-posting-onsite-apply-configuration
- name: QuestionChoice
  property_count: 2
  slug: linkedin-talent-job-posting-question-choice
- name: QuestionDetails
  property_count: 1
  slug: linkedin-talent-job-posting-question-details
- name: ResumeQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-resume-questions
- name: SimpleJobPostingRequest
  property_count: 1
  slug: linkedin-talent-job-posting-simple-job-posting-request
- name: WorkQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-work-questions
- name: ApplicationCredentials
  property_count: 4
  slug: linkedin-talent-learning-parent-application-application-credentials
- name: ErrorResponse
  property_count: 3
  slug: linkedin-talent-learning-parent-application-error-response
- name: GetApplicationResponse
  property_count: 1
  slug: linkedin-talent-learning-parent-application-get-application-response
- name: ProvisionApplicationRequest
  property_count: 5
  slug: linkedin-talent-learning-parent-application-provision-application-request
- name: ProvisionApplicationResponse
  property_count: 8
  slug: linkedin-talent-learning-parent-application-provision-application-response
- name: UpdateCallbackUrlRequest
  property_count: 1
  slug: linkedin-talent-learning-parent-application-update-callback-url-request
- name: AccessTokenRequest
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-request
- name: AccessTokenResponse
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-response
- name: Address
  property_count: 6
  slug: linkedin-talent-recruiter-system-connect-address
- name: ApplicationData
  property_count: 10
  slug: linkedin-talent-recruiter-system-connect-application-data
- name: ApplicationRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-application-request
- name: AtsIntegrationUpdateRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request
- name: CandidateData
  property_count: 13
  slug: linkedin-talent-recruiter-system-connect-candidate-data
- name: CandidateRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-candidate-request
- name: ConfigurationValue
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-configuration-value
- name: IntegrationConfigurationRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request
- name: IntegrationPatch
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-patch
- name: NoteData
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-note-data
- name: NoteRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-note-request
- name: PersonName
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-person-name
- name: PhoneNumber
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-phone-number
- name: TargetingCriteria
  property_count: 1
  slug: linkedin-targetingcriteria
- name: Timestamp
  property_count: 1
  slug: linkedin-timestamp
- name: UpdateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-updateadynamicspotlightrequest
- name: UpdateAPostRequest
  property_count: 0
  slug: linkedin-updateapostrequest
- name: UpdateASponsoredConversationRequest
  property_count: 0
  slug: linkedin-updateasponsoredconversationrequest
- name: UpdateCallbackUrlRequest
  property_count: 1
  slug: linkedin-updatecallbackurlrequest
- name: UpdateInmailContentRequest
  property_count: 0
  slug: linkedin-updateinmailcontentrequest
- name: UpdateSponsoredMessageContentRequest
  property_count: 0
  slug: linkedin-updatesponsoredmessagecontentrequest
- name: UserId
  property_count: 2
  slug: linkedin-userid
- name: UserStreamElement
  property_count: 2
  slug: linkedin-userstreamelement
- name: UserStreamRequest
  property_count: 1
  slug: linkedin-userstreamrequest
- name: ValidateTheUsersOrganizationResponse200
  property_count: 2
  slug: linkedin-validatetheusersorganizationresponse200
- name: WorkQuestions
  property_count: 1
  slug: linkedin-workquestions
json_structures:
- name: Linkedin Compliance Events Compliance Authorization Request Structure
  property_count: 1
  slug: linkedin-compliance-events-compliance-authorization-request-structure
- name: Linkedin Compliance Events Compliance Authorization Response Structure
  property_count: 2
  slug: linkedin-compliance-events-compliance-authorization-response-structure
- name: Linkedin Compliance Events Compliance Authorization Structure
  property_count: 4
  slug: linkedin-compliance-events-compliance-authorization-structure
- name: Linkedin Compliance Events Compliance Event Structure
  property_count: 15
  slug: linkedin-compliance-events-compliance-event-structure
- name: Linkedin Compliance Events Compliance Events Response Structure
  property_count: 2
  slug: linkedin-compliance-events-compliance-events-response-structure
- name: Linkedin Compliance Events Error Response Structure
  property_count: 3
  slug: linkedin-compliance-events-error-response-structure
- name: Linkedin Compliance Events Member Profile Structure
  property_count: 3
  slug: linkedin-compliance-events-member-profile-structure
- name: Linkedin Compliance Events Paging Link Structure
  property_count: 3
  slug: linkedin-compliance-events-paging-link-structure
- name: Linkedin Compliance Events Paging Structure
  property_count: 4
  slug: linkedin-compliance-events-paging-structure
- name: Linkedin Learning Activity Reports Error Response Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-error-response-structure
- name: Linkedin Learning Activity Reports Learner Details Structure
  property_count: 1
  slug: linkedin-learning-activity-reports-learner-details-structure
- name: Linkedin Learning Activity Reports Learner Entity Structure
  property_count: 4
  slug: linkedin-learning-activity-reports-learner-entity-structure
- name: Linkedin Learning Activity Reports Learning Activity Report Response Structure
  property_count: 2
  slug: linkedin-learning-activity-reports-learning-activity-report-response-structure
- name: Linkedin Learning Activity Reports Learning Activity Report Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-learning-activity-report-structure
- name: Linkedin Learning Activity Reports Learning Activity Structure
  property_count: 6
  slug: linkedin-learning-activity-reports-learning-activity-structure
- name: Linkedin Learning Activity Reports Paging Link Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-paging-link-structure
- name: Linkedin Learning Activity Reports Paging Structure
  property_count: 4
  slug: linkedin-learning-activity-reports-paging-structure
- name: Linkedin Marketing Audience Ad Account Structure
  property_count: 4
  slug: linkedin-marketing-audience-ad-account-structure
- name: Linkedin Marketing Audience Ad Accounts Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-ad-accounts-response-structure
- name: Linkedin Marketing Audience Company Stream Element Structure
  property_count: 4
  slug: linkedin-marketing-audience-company-stream-element-structure
- name: Linkedin Marketing Audience Company Stream Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-company-stream-request-structure
- name: Linkedin Marketing Audience Dmp Segment Create Request Structure
  property_count: 6
  slug: linkedin-marketing-audience-dmp-segment-create-request-structure
- name: Linkedin Marketing Audience Dmp Segment Structure
  property_count: 11
  slug: linkedin-marketing-audience-dmp-segment-structure
- name: Linkedin Marketing Audience Dmp Segments Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-dmp-segments-response-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Entities Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Entity Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-ad-targeting-entity-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Facet Structure
  property_count: 4
  slug: linkedin-marketing-audience-insights-ad-targeting-facet-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Facets Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response-structure
- name: Linkedin Marketing Audience Insights Audience Insight Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-audience-insight-structure
- name: Linkedin Marketing Audience Insights Audience Insights Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-request-structure
- name: Linkedin Marketing Audience Insights Audience Insights Response Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-response-structure
- name: Linkedin Marketing Audience Insights Error Response Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-error-response-structure
- name: Linkedin Marketing Audience Insights Insight Segmentation Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-insight-segmentation-structure
- name: Linkedin Marketing Audience Insights Paging Link Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-paging-link-structure
- name: Linkedin Marketing Audience Insights Paging Structure
  property_count: 4
  slug: linkedin-marketing-audience-insights-paging-structure
- name: Linkedin Marketing Audience Insights Request Meta Data Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-request-meta-data-structure
- name: Linkedin Marketing Audience Insights Targeting Criteria Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-targeting-criteria-structure
- name: Linkedin Marketing Audience List Upload Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-list-upload-request-structure
- name: Linkedin Marketing Audience Paging Structure
  property_count: 4
  slug: linkedin-marketing-audience-paging-structure
- name: Linkedin Marketing Audience Segment Destination Structure
  property_count: 1
  slug: linkedin-marketing-audience-segment-destination-structure
- name: Linkedin Marketing Audience Stream Response Structure
  property_count: 1
  slug: linkedin-marketing-audience-stream-response-structure
- name: Linkedin Marketing Audience Stream Result Element Structure
  property_count: 1
  slug: linkedin-marketing-audience-stream-result-element-structure
- name: Linkedin Marketing Audience User Id Structure
  property_count: 2
  slug: linkedin-marketing-audience-user-id-structure
- name: Linkedin Marketing Audience User Stream Element Structure
  property_count: 2
  slug: linkedin-marketing-audience-user-stream-element-structure
- name: Linkedin Marketing Audience User Stream Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-user-stream-request-structure
- name: Linkedin Marketing Campaigns Ad Account Create Request Structure
  property_count: 9
  slug: linkedin-marketing-campaigns-ad-account-create-request-structure
- name: Linkedin Marketing Campaigns Ad Account Structure
  property_count: 11
  slug: linkedin-marketing-campaigns-ad-account-structure
- name: Linkedin Marketing Campaigns Ad Account User Create Request Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-create-request-structure
- name: Linkedin Marketing Campaigns Ad Account User Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-structure
- name: Linkedin Marketing Campaigns Ad Account User Update Request Structure
  property_count: 1
  slug: linkedin-marketing-campaigns-ad-account-user-update-request-structure
- name: Linkedin Marketing Campaigns Audience Count Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-audience-count-structure
- name: Linkedin Marketing Campaigns Budget Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-budget-structure
- name: Linkedin Marketing Campaigns Campaign Group Structure
  property_count: 6
  slug: linkedin-marketing-campaigns-campaign-group-structure
- name: Linkedin Marketing Campaigns Campaign Structure
  property_count: 10
  slug: linkedin-marketing-campaigns-campaign-structure
- name: Linkedin Marketing Campaigns Campaign Update Request Structure
  property_count: 1
  slug: linkedin-marketing-campaigns-campaign-update-request-structure
- name: Linkedin Marketing Campaigns Creative Create Request Structure
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-create-request-structure
- name: Linkedin Marketing Campaigns Creative Structure
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-structure
- name: Linkedin Marketing Campaigns Organization Acl Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-organization-acl-structure
- name: Linkedin Marketing Campaigns Paging Structure
  property_count: 4
  slug: linkedin-marketing-campaigns-paging-structure
- name: Linkedin Marketing Campaigns Run Schedule Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-run-schedule-structure
- name: Linkedin Marketing Community Batch Get On Administered Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-administered-response200-structure
- name: Linkedin Marketing Community Batch Get On Nonadministered Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200-structure
- name: Linkedin Marketing Community Find Administered Organization Brands Response200 Structure
  property_count: 2
  slug: linkedin-marketing-community-find-administered-organization-brands-response200-structure
- name: Linkedin Marketing Community Find Nonadministered Organization Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-find-nonadministered-organization-response200-structure
- name: Linkedin Marketing Community Lookup By Organization Primary Response200 Structure
  property_count: 1
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200-structure
- name: Linkedin Marketing Community Retrieve An Administered Organization Response200 Structure
  property_count: 16
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200-structure
- name: Linkedin Marketing Community Retrieve Organization Follower Count Response200 Structure
  property_count: 1
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200-structure
- name: Linkedin Marketing Conversions Create A New Conversion Response201 Structure
  property_count: 14
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201-structure
- name: Linkedin Marketing Conversions Fetch Active Campaigns Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200-structure
- name: Linkedin Marketing Conversions Fetch Existing Conversion Rules Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200-structure
- name: Linkedin Marketing Conversions Retrieve Authenticated Users Sponsored Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200-structure
- name: Linkedin Marketing Conversions Stream Multiple Conversion Events Response200 Structure
  property_count: 1
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200-structure
- name: Linkedin Marketing Leads Fetch Full Lead Data Response200 Structure
  property_count: 10
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200-structure
- name: Linkedin Marketing Leads Get Forms For The Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-get-forms-for-the-response200-structure
- name: Linkedin Marketing Leads Get The Users Sponsored Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200-structure
- name: Linkedin Marketing Leads Validate The Users Organization Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-validate-the-users-organization-response200-structure
- name: Linkedin Marketing Media Planning Get A List Of Response200 Structure
  property_count: 2
  slug: linkedin-marketing-media-planning-get-a-list-of-response200-structure
- name: Linkedin Marketing Media Planning Get Bing Geo Locations Response200 Structure
  property_count: 2
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200-structure
- name: Linkedin Marketing Reporting Roi Conversions By Member Company Response200 Structure
  property_count: 2
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200-structure
- name: Linkedin Regulations Data Portability Address Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-address-structure
- name: Linkedin Regulations Data Portability Batch Organization Response Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-batch-organization-response-structure
- name: Linkedin Regulations Data Portability Date Info Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-date-info-structure
- name: Linkedin Regulations Data Portability Image Asset Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-image-asset-structure
- name: Linkedin Regulations Data Portability Image Reference Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-image-reference-structure
- name: Linkedin Regulations Data Portability Locale Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-locale-structure
- name: Linkedin Regulations Data Portability Localized String Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-localized-string-structure
- name: Linkedin Regulations Data Portability Organization Acl Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-organization-acl-response-structure
- name: Linkedin Regulations Data Portability Organization Acl Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-acl-structure
- name: Linkedin Regulations Data Portability Organization Location Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-location-structure
- name: Linkedin Regulations Data Portability Organization Response Structure
  property_count: 18
  slug: linkedin-regulations-data-portability-organization-response-structure
- name: Linkedin Regulations Data Portability Post Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-post-response-structure
- name: Linkedin Regulations Data Portability Post Structure
  property_count: 7
  slug: linkedin-regulations-data-portability-post-structure
- name: Linkedin Regulations Data Portability Reaction Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-reaction-response-structure
- name: Linkedin Regulations Data Portability Timestamp Structure
  property_count: 1
  slug: linkedin-regulations-data-portability-timestamp-structure
- name: Linkedin Regulatory Ads Transparency Advertiser Transparency Request Structure
  property_count: 2
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request-structure
- name: Linkedin Regulatory Ads Transparency Advertiser Transparency Response Structure
  property_count: 7
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response-structure
- name: Linkedin Regulatory Ads Transparency Error Response Structure
  property_count: 3
  slug: linkedin-regulatory-ads-transparency-error-response-structure
- name: Linkedin Sales Navigator Batch Profile Association Response Structure
  property_count: 3
  slug: linkedin-sales-navigator-batch-profile-association-response-structure
- name: Linkedin Sales Navigator Contract Structure
  property_count: 4
  slug: linkedin-sales-navigator-contract-structure
- name: Linkedin Sales Navigator Contracts Response Structure
  property_count: 2
  slug: linkedin-sales-navigator-contracts-response-structure
- name: Linkedin Sales Navigator Crm Data Validation Export Job Request Structure
  property_count: 1
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request-structure
- name: Linkedin Sales Navigator Crm Data Validation Export Job Structure
  property_count: 7
  slug: linkedin-sales-navigator-crm-data-validation-export-job-structure
- name: Linkedin Sales Navigator Error Response Structure
  property_count: 3
  slug: linkedin-sales-navigator-error-response-structure
- name: Linkedin Sales Navigator Paging Structure
  property_count: 3
  slug: linkedin-sales-navigator-paging-structure
- name: Linkedin Sales Navigator Sales Access Token Response Structure
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-response-structure
- name: Linkedin Sales Navigator Sales Access Token Structure
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Request Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-analytics-export-job-request-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Response Structure
  property_count: 1
  slug: linkedin-sales-navigator-sales-analytics-export-job-response-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Structure
  property_count: 5
  slug: linkedin-sales-navigator-sales-analytics-export-job-structure
- name: Linkedin Sales Navigator Sales Navigator Profile Association Key Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key-structure
- name: Linkedin Sales Navigator Sales Navigator Profile Association Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-structure
- name: Linkedin Structure
  property_count: 0
  slug: linkedin-structure
- name: Linkedin Talent Job Posting Additional Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-additional-questions-structure
- name: Linkedin Talent Job Posting Application Questions Structure
  property_count: 6
  slug: linkedin-talent-job-posting-application-questions-structure
- name: Linkedin Talent Job Posting Cover Letter Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-cover-letter-questions-structure
- name: Linkedin Talent Job Posting Custom Question Set Structure
  property_count: 2
  slug: linkedin-talent-job-posting-custom-question-set-structure
- name: Linkedin Talent Job Posting Custom Question Structure
  property_count: 4
  slug: linkedin-talent-job-posting-custom-question-structure
- name: Linkedin Talent Job Posting Education Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-education-questions-structure
- name: Linkedin Talent Job Posting Job Posting Element Structure
  property_count: 10
  slug: linkedin-talent-job-posting-job-posting-element-structure
- name: Linkedin Talent Job Posting Job Posting Response Structure
  property_count: 1
  slug: linkedin-talent-job-posting-job-posting-response-structure
- name: Linkedin Talent Job Posting Multiple Choice Question Details Structure
  property_count: 3
  slug: linkedin-talent-job-posting-multiple-choice-question-details-structure
- name: Linkedin Talent Job Posting Onsite Apply Configuration Structure
  property_count: 2
  slug: linkedin-talent-job-posting-onsite-apply-configuration-structure
- name: Linkedin Talent Job Posting Question Choice Structure
  property_count: 2
  slug: linkedin-talent-job-posting-question-choice-structure
- name: Linkedin Talent Job Posting Question Details Structure
  property_count: 1
  slug: linkedin-talent-job-posting-question-details-structure
- name: Linkedin Talent Job Posting Resume Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-resume-questions-structure
- name: Linkedin Talent Job Posting Simple Job Posting Request Structure
  property_count: 1
  slug: linkedin-talent-job-posting-simple-job-posting-request-structure
- name: Linkedin Talent Job Posting Work Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-work-questions-structure
- name: Linkedin Talent Learning Parent Application Application Credentials Structure
  property_count: 4
  slug: linkedin-talent-learning-parent-application-application-credentials-structure
- name: Linkedin Talent Learning Parent Application Error Response Structure
  property_count: 3
  slug: linkedin-talent-learning-parent-application-error-response-structure
- name: Linkedin Talent Learning Parent Application Get Application Response Structure
  property_count: 1
  slug: linkedin-talent-learning-parent-application-get-application-response-structure
- name: Linkedin Talent Learning Parent Application Provision Application Request Structure
  property_count: 5
  slug: linkedin-talent-learning-parent-application-provision-application-request-structure
- name: Linkedin Talent Learning Parent Application Provision Application Response Structure
  property_count: 8
  slug: linkedin-talent-learning-parent-application-provision-application-response-structure
- name: Linkedin Talent Learning Parent Application Update Callback Url Request Structure
  property_count: 1
  slug: linkedin-talent-learning-parent-application-update-callback-url-request-structure
- name: Linkedin Talent Recruiter System Connect Access Token Request Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-request-structure
- name: Linkedin Talent Recruiter System Connect Access Token Response Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-response-structure
- name: Linkedin Talent Recruiter System Connect Address Structure
  property_count: 6
  slug: linkedin-talent-recruiter-system-connect-address-structure
- name: Linkedin Talent Recruiter System Connect Application Data Structure
  property_count: 10
  slug: linkedin-talent-recruiter-system-connect-application-data-structure
- name: Linkedin Talent Recruiter System Connect Application Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-application-request-structure
- name: Linkedin Talent Recruiter System Connect Ats Integration Update Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request-structure
- name: Linkedin Talent Recruiter System Connect Candidate Data Structure
  property_count: 13
  slug: linkedin-talent-recruiter-system-connect-candidate-data-structure
- name: Linkedin Talent Recruiter System Connect Candidate Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-candidate-request-structure
- name: Linkedin Talent Recruiter System Connect Configuration Value Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-configuration-value-structure
- name: Linkedin Talent Recruiter System Connect Integration Configuration Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request-structure
- name: Linkedin Talent Recruiter System Connect Integration Patch Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-patch-structure
- name: Linkedin Talent Recruiter System Connect Note Data Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-note-data-structure
- name: Linkedin Talent Recruiter System Connect Note Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-note-request-structure
- name: Linkedin Talent Recruiter System Connect Person Name Structure
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-person-name-structure
- name: Linkedin Talent Recruiter System Connect Phone Number Structure
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-phone-number-structure
jsonld:
- class_count: 132
  name: Linkedin Api Context
  property_count: 265
  slug: linkedin-api-context
layout: provider
mcp_servers:
- description: ''
  name: linkedin-mcp.yml
  slug: linkedin-mcpyml
modified: '2026-06-20'
name: LinkedIn
nav: Providers
network: true
overview: 'LinkedIn publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Consumer API, Access Control API, Account Management API, and 62 more. Tagged areas include Business, Careers, Marketing, Professional Networking, and Recruiting.


  The LinkedIn catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  LinkedIn''s developer surface includes changelog, authentication, documentation, code examples, developer portal, signup flow, tooling, and 78 more developer resources.'
plans:
- name: Linkedin Plans Pricing
  plan_count: 8
  slug: linkedin-plans-pricing
press:
- date: '2026-05-25'
  title: LinkedIn Pressroom | LinkedIn
  url: https://news.linkedin.com/
- date: '2026-05-25'
  title: Why using AI to write your press release could be hurting ...
  url: https://www.linkedin.com/pulse/why-using-ai-write-your-press-release-could-hurting-brand-dybac-brpac
- date: '2026-05-25'
  title: (PDF) The Rise of AI-Generated Content on LinkedIn
  url: https://www.researchgate.net/publication/391873822_The_Rise_of_AI-Generated_Content_on_LinkedIn_Implications_for_Engagement_Trust_and_Thought_Leadership
- date: '2026-05-25'
  title: Artificial Intelligence News
  url: https://www.linkedin.com/showcase/artificial-intelligence-news/
- date: '2026-05-25'
  title: AI's Impact on Local News Production
  url: https://www.linkedin.com/top-content/artificial-intelligence/ai-in-journalism/ai-s-impact-on-local-news-production/
random_paper: 55
rate_limits:
- limit_count: 3
  name: Linkedin Rate Limits
  slug: linkedin-rate-limits
rules:
- name: LinkedIn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: linkedin-jsonschema-spectral-rules
- name: LinkedIn API Rules
  rule_count: 28
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 10
  slug: linkedin-spectral-rules
scopes:
- name: Linkedin Scopes
  scope_count: 7
  slug: linkedin-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 70.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 78.0
    developer_ergonomics: 63.0
    discoverability: 87.0
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 64
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkedin/refs/heads/main/screenshots/linkedin-2026-06-20T184544.png
security:
- kind: authentication
  name: Linkedin Authentication
  slug: linkedin-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Linkedin Domain Security
  slug: linkedin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linkedin Vulnerability Disclosure
  slug: linkedin-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: linkedin
solutions:
- description: Sign In with LinkedIn, Share on LinkedIn, and Verified on LinkedIn for consumer-facing integrations.
  name: Consumer Solutions
- description: B2B advertising platform with campaign management, audience targeting, lead generation, and analytics.
  name: Marketing Solutions
- description: Job posting, recruiter system connect, and apply with LinkedIn for talent acquisition and ATS integration.
  name: Talent Solutions
- description: LinkedIn Learning integration for employee development tracking, content access, and activity reporting.
  name: Learning Solutions
- description: LinkedIn Sales Navigator API for CRM sync, display services, and sales analytics.
  name: Sales Solutions
- description: Message archiving and activity monitoring for regulated industries requiring communications governance.
  name: Compliance Solutions
- description: Data portability and advertiser transparency APIs for Digital Markets Act and regulatory compliance.
  name: Regulatory Solutions
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
- Fortune 1000
use_cases:
- description: Implement Sign In with LinkedIn for professional identity verification and streamlined authentication.
  name: Social Login
- description: Create and manage targeted advertising campaigns reaching professional audiences by industry, job title, and company.
  name: B2B Advertising
- description: Retrieve campaign performance metrics, audience insights, and conversion attribution for marketing optimization.
  name: Marketing Analytics
- description: Post jobs, manage candidates, and integrate ATS systems with LinkedIn Recruiter for streamlined hiring.
  name: Talent Acquisition
- description: Integrate CRM systems with LinkedIn Sales Navigator for lead enrichment and relationship insights.
  name: Sales Intelligence
- description: Track and report on LinkedIn Learning usage, completions, and skill development across organizations.
  name: Employee Learning
- description: Archive communications and activities on LinkedIn for compliance with financial industry regulations.
  name: Regulatory Compliance
- description: Automate sharing of articles, updates, and media content to LinkedIn feeds and company pages.
  name: Content Distribution
website: https://www.linkedin.com/developers/
---
