---
aid: linkedin
name: LinkedIn
description: LinkedIn is a professional networking platform providing APIs for consumer integrations (Sign In, Share, Verified on LinkedIn), marketing solutions (ad campaigns, audiences, conversions, analytics), talent solutions (job posting, recruiter system connect), learning solutions (activity reports, content), sales navigator (CRM sync, display, analytics), compliance (message archiving), and regulatory data portability.
type: Index
image: https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg
url: https://raw.githubusercontent.com/api-evangelist/linkedin/refs/heads/main/apis.yml
created: '2024-04-14'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Business
  - Careers
  - Marketing
  - Professional Networking
  - Recruiting
  - Social Media
apis:
  - aid: linkedin:linkedin-consumer-api
    name: LinkedIn Consumer API
    tags:
      - Authentication
      - Sharing
      - Social
      - Verification
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/consumer/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/getting-started
        type: GettingStarted
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/verified-on-linkedin
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api
        type: APIReference
      - url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-consumer-solutions/overview
        type: PostmanWorkspace
    description: The LinkedIn Consumer Solutions Platform enables sites and applications the power to enhance their sign-in experience using the world's largest professional network. The Consumer Solutions Platform contains APIs to Sign In with LinkedIn, Share on LinkedIn, and Verified on LinkedIn. Follow the links below to learn more about the Consumer Solutions Platform APIs.
  - aid: linkedin:linkedin-marketing-api
    name: LinkedIn Marketing API
    tags:
      - Advertising
      - Analytics
      - Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/marketing/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/getting-started
        type: GettingStarted
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/usecases/
        type: UseCases
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes
        type: ChangeLog
      - url: openapi/linkedin-marketing-audience-insights.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-audience.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-campaigns.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-community.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-content.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-conversions.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-leads.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-media-planning.yml
        type: OpenAPI
      - url: openapi/linkedin-marketing-reporting-roi.yml
        type: OpenAPI
      - url: https://learn.microsoft.com/en-us/linkedin/marketing/lms-faq
        type: FAQ
      - url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-marketing-solutions-versioned-apis/overview
        type: PostmanWorkspace
    description: Grow your business by building scalable solutions that drive workflow efficiency, streamline marketing activities, deliver unique insights, and maximize results for B2B marketers.
  - aid: linkedin:linkedin-learning-solutions
    name: LinkedIn Learning Solutions
    tags:
      - Education
      - Learning
      - Training
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/learning/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/learning/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/learning/getting-started
        type: GettingStarted
      - url: https://learn.microsoft.com/en-us/linkedin/learning/getting-started/terminology
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/learning/integrations/release-notes
        type: ReleaseNotes
      - url: https://learn.microsoft.com/en-us/linkedin/learning/integrations/xapi
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/learning/reporting/reporting-docs/reporting-api
        type: APIReference
      - url: openapi/linkedin-learning-activity-reports.yml
        type: OpenAPI
      - url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-learning-solutions/overview
        type: PostmanWorkspace
    description: LinkedIn Learning is an online learning platform that combines the industry-leading content from Lynda.com with LinkedIn's professional data and network.
  - aid: linkedin:linkedin-talent-solutions
    name: LinkedIn Talent Solutions
    tags:
      - Hiring
      - Recruiting
      - Talent
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/talent/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/talent/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/talent/getting-started
        type: GettingStarted
      - url: openapi/linkedin-talent-job-posting.yml
        type: OpenAPI
      - url: openapi/linkedin-talent-learning-parent-application.yml
        type: OpenAPI
      - url: https://learn.microsoft.com/en-us/linkedin/talent/release-notes
        type: ReleaseNotes
      - url: https://learn.microsoft.com/en-us/linkedin/talent/versioning
        type: Documentation
      - url: openapi/linkedin-talent-recruiter-system-connect.yml
        type: OpenAPI
      - url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-talent-solutions/overview
        type: PostmanWorkspace
    description: The LinkedIn Talent Solutions enhances candidate sourcing and recruiting experience for ATSs and applications using the world's largest professional network. Follow the links below to learn more about the LinkedIn Talent Solutions APIs.
  - aid: linkedin:linkedin-compliance-solutions
    name: LinkedIn Compliance Solutions
    tags:
      - Archiving
      - Compliance
      - Governance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/compliance/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/compliance/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/compliance/getting-started
        type: GettingStarted
      - url: https://learn.microsoft.com/en-us/linkedin/compliance/release-notes
        type: ReleaseNotes
      - url: https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/compliance-faq
        type: FAQ
      - url: https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/overview
        type: Documentation
      - url: openapi/linkedin-compliance-events.yml
        type: OpenAPI
      - url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-compliance-solutions/overview
        type: PostmanWorkspace
    description: LinkedIn provides the following Compliance API Guides for all monitoring, archiving, and management of communications for enterprises in regulated industries. The APIs will help your social interactions remain effective while ensuring compliance with corporate governance policies and major regulations.
  - aid: linkedin:linkedin-sales-navigator-api
    name: LinkedIn Sales Navigator API
    tags:
      - CRM
      - Sales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/sales/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/sales/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/sales/display-services/
        type: APIReference
      - url: https://learn.microsoft.com/en-us/linkedin/sales/analytics-services/
        type: APIReference
      - url: https://learn.microsoft.com/en-us/linkedin/sales/sync-services/
        type: APIReference
      - url: openapi/linkedin-sales-navigator.yml
        type: OpenAPI
    description: LinkedIn Sales Navigator is a leading social selling tool that builds and nurtures customer relationships to lead to increased sales performance. By leveraging the power of LinkedIn's Sales Navigator, you can add exposure to sales leaders who are already engaged on LinkedIn and increase your product's engagement by integrating LinkedIn Sales Navigator seamlessly into your customers' workflow.
  - aid: linkedin:linkedin-regulatory-api
    name: LinkedIn Regulatory API
    tags:
      - Compliance
      - Regulatory
      - Transparency
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linkedin.com
    humanURL: https://learn.microsoft.com/en-us/linkedin/dma/
    properties:
      - url: https://learn.microsoft.com/en-us/linkedin/dma/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/dma/pages-data-portability-overview
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/dma/transparency/advertiser-transparency
        type: Documentation
      - url: https://learn.microsoft.com/en-us/linkedin/dma/transparency/advertiser-transparency-faq
        type: FAQ
      - url: https://learn.microsoft.com/en-us/linkedin/dma/recent-changes
        type: ChangeLog
      - url: openapi/linkedin-regulations-data-portability.yml
        type: OpenAPI
      - url: openapi/linkedin-regulatory-ads-transparency.yml
        type: OpenAPI
    description: LinkedIn Regulatory APIs provide access to data portability and ads transparency capabilities for regulatory compliance, including the Digital Markets Act (DMA) requirements for organization data portability and advertiser transparency reporting.
common:
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
    type: Authentication
  - url: https://www.linkedin.com/oauth/.well-known/openid-configuration
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/sample-applications
    type: CodeExamples
  - url: https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/marketing/versioning
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/overview
    type: BestPractices
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts?context=linkedin/consumer/context
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin/consumer/context
    type: Documentation
  - url: https://docs.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
    type: RateLimits
  - url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/plugins?context=linkedin/consumer/context
    type: Documentation
  - url: https://www.linkedin.com/developers/
    type: Portal
  - url: https://www.linkedin.com/developers/apps
    type: SignUp
  - url: https://www.linkedin.com/developers/tools/oauth
    type: Tools
  - url: https://www.linkedin-apistatus.com/
    type: StatusPage
  - url: https://www.linkedin.com/content/developers/news
    type: Blog
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools
    type: Tools
  - url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation
    type: Documentation
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development
    type: BestPractices
  - url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications
    type: BestPractices
  - url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients
    type: SDK
  - url: https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api
    type: APIReference
  - url: https://github.com/linkedin-developers
    type: GitHubOrganization
  - url: https://github.com/linkedin-developers/linkedin-api-js-client
    type: SDK
  - url: https://github.com/linkedin-developers/linkedin-api-python-client
    type: SDK
  - url: https://developer.linkedin.com/support
    type: Support
  - url: https://github.com/linkedin-developers/linkedin-capi-tag-template
    type: Tools
    description: Google Tag Manager template for streaming conversion events to LinkedIn's Conversions API.
  - url: https://github.com/linkedin-developers/java-sample-application
    type: CodeExamples
    description: Official Java sample application for LinkedIn APIs.
  - url: https://www.linkedin.com/legal/api-terms-of-use
    type: TermsOfService
  - url: https://www.linkedin.com/legal/privacy-policy
    type: PrivacyPolicy
  - type: Features
    data:
      - name: Sign In with LinkedIn
        description: OpenID Connect-based authentication enabling users to sign in to third-party applications with their LinkedIn credentials.
      - name: Share on LinkedIn
        description: Enable users to share content from your application directly to their LinkedIn feed.
      - name: Verified on LinkedIn
        description: Display verified professional credentials and certifications from LinkedIn on third-party platforms.
      - name: Campaign Management
        description: Programmatically create, manage, and optimize B2B advertising campaigns with targeting and budget controls.
      - name: Audience Insights
        description: Access aggregated audience demographics and firmographic data for ad targeting and market research.
      - name: Conversions API
        description: Send online and offline conversion events for attribution and campaign optimization.
      - name: Lead Gen Forms
        description: Collect leads directly from LinkedIn ads with pre-filled forms using member profile data.
      - name: Job Posting
        description: Programmatically publish and manage job listings on LinkedIn through the Talent Solutions API.
      - name: Recruiter System Connect
        description: Integrate applicant tracking systems with LinkedIn Recruiter for seamless candidate management.
      - name: Learning Activity Reports
        description: Retrieve learner engagement, completions, and activity data from LinkedIn Learning.
      - name: Compliance Archiving
        description: Archive and monitor LinkedIn messages and activities for regulatory compliance in regulated industries.
      - name: Data Portability
        description: Access member and organization data portability endpoints for Digital Markets Act compliance.
  - type: UseCases
    data:
      - name: Social Login
        description: Implement Sign In with LinkedIn for professional identity verification and streamlined authentication.
      - name: B2B Advertising
        description: Create and manage targeted advertising campaigns reaching professional audiences by industry, job title, and company.
      - name: Marketing Analytics
        description: Retrieve campaign performance metrics, audience insights, and conversion attribution for marketing optimization.
      - name: Talent Acquisition
        description: Post jobs, manage candidates, and integrate ATS systems with LinkedIn Recruiter for streamlined hiring.
      - name: Sales Intelligence
        description: Integrate CRM systems with LinkedIn Sales Navigator for lead enrichment and relationship insights.
      - name: Employee Learning
        description: Track and report on LinkedIn Learning usage, completions, and skill development across organizations.
      - name: Regulatory Compliance
        description: Archive communications and activities on LinkedIn for compliance with financial industry regulations.
      - name: Content Distribution
        description: Automate sharing of articles, updates, and media content to LinkedIn feeds and company pages.
  - type: Integrations
    data:
      - name: Salesforce
        description: LinkedIn Sales Navigator integration with Salesforce CRM for lead and account synchronization.
      - name: Microsoft Dynamics
        description: Native integration with Microsoft Dynamics 365 for sales intelligence and lead management.
      - name: HubSpot
        description: LinkedIn Ads integration with HubSpot for campaign management and lead synchronization.
      - name: Postman
        description: Official Postman workspaces for all LinkedIn API business lines with pre-built collections.
      - name: OpenID Connect
        description: Standards-based authentication using OpenID Connect for Sign In with LinkedIn.
  - type: Solutions
    data:
      - name: Consumer Solutions
        description: Sign In with LinkedIn, Share on LinkedIn, and Verified on LinkedIn for consumer-facing integrations.
      - name: Marketing Solutions
        description: B2B advertising platform with campaign management, audience targeting, lead generation, and analytics.
      - name: Talent Solutions
        description: Job posting, recruiter system connect, and apply with LinkedIn for talent acquisition and ATS integration.
      - name: Learning Solutions
        description: LinkedIn Learning integration for employee development tracking, content access, and activity reporting.
      - name: Sales Solutions
        description: LinkedIn Sales Navigator API for CRM sync, display services, and sales analytics.
      - name: Compliance Solutions
        description: Message archiving and activity monitoring for regulated industries requiring communications governance.
      - name: Regulatory Solutions
        description: Data portability and advertiser transparency APIs for Digital Markets Act and regulatory compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
