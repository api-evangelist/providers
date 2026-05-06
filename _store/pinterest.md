---
aid: pinterest
url: https://raw.githubusercontent.com/api-search/images/main/_apis/pinterest/apis.md
apis:
  - aid: pinterest:pinterest-api
    name: Pinterest API
    tags:
      - Images
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.pinterest.com/v5
    humanURL: https://developers.pinterest.com/
    properties:
      - url: https://developers.pinterest.com/docs/api/v5/
        type: Documentation
      - url: openapi/pinterest-openapi-original.yml
        type: OpenAPI
    description: The Pinterest REST API v5 for managing ads, ad groups, ad accounts, audiences, billing, boards, board sections, pins, catalogs, and analytics on Pinterest.
name: Pinterest
tags:
  - Images
  - Social Media
  - Videos
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.pinterest.com/_/_/policy/developer-guidelines
    type: Guidelines
  - url: https://www.pinterest.com/_/_/newsroom/
    type: News
  - url: https://medium.com/pinterest-engineering
    type: Blog
  - url: https://help.pinterest.com/contact
    type: Support
  - url: https://developers.pinterest.com/terms/
    type: Terms of Service
  - url: https://github.com/pinterest/api-description
    type: OpenAPI
  - url: https://github.com/pinterest
    type: GitHub Org
  - url: https://www.pintereststatus.com/
    name: Status
    type: Status
  - url: https://developers.pinterest.com/
    name: Pinterest Developers
    type: Portal
    description: 'null'
  - url: https://developers.pinterest.com/docs/overview/welcome/
    name: Pinterest Developers
    type: Documentation
    description: 'null'
  - url: https://developers.pinterest.com/docs/changelog/changelog/
    name: Pinterest Developers
    type: ChangeLog
    description: 'null'
  - url: https://developers.pinterest.com/docs/getting-started/connect-app/
    name: Pinterest Developers
    type: GettingStarted
    description: 'null'
  - url: https://developers.pinterest.com/docs/api-features/track-conversion-events/
    name: Pinterest Developers
    type: Features
    description: 'null'
    data:
      - 'Pinterest: hundreds of services across Social Media + Ads'
      - 'Detailed pricing: see https://developers.pinterest.com/docs/api/v5/introduction/'
      - 'Service: Pinterest API v5 (free for OAuth-authorized apps)'
      - 'Service: Marketing API (Ads Manager)'
      - 'Service: Catalogs API (commerce)'
      - 'Service: Conversions API (server-side events)'
      - 'Service: Trial of Pinterest Plus / Premiere'
    sources:
      - https://developers.pinterest.com/docs/api/v5/introduction/
      - https://focus.finops.org/
    updated: '2026-05-04'
  - url: https://developers.pinterest.com/docs/developer-tools/sdk/
    name: Pinterest Developers
    type: SDKs
    description: Developer
  - url: https://developers.pinterest.com/docs/developer-tools/sandbox/
    name: Pinterest Developers
    type: Sandbox
    description: Developer
  - url: https://developers.pinterest.com/docs/developer-tools/quickstart-tools/
    name: Pinterest Developers
    type: GettingStarted
    description: Developer
  - url: https://developers.pinterest.com/docs/reference/rate-limits/
    name: Pinterest Developers
    type: RateLimits
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/error-codes/
    name: Pinterest Developers
    type: Errors
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/pagination/
    name: Pinterest Developers
    type: Pagination
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/help-and-feedback/
    name: Pinterest Developers
    type: Support
    description: 'null'
  - url: https://developers.pinterest.com/terms/
    name: Pinterest Developers | Terms
    type: TermsOfService
    description: 'null'
  - url: https://policy.pinterest.com/en/privacy-policy
    name: Privacy Policy | Pinterest Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://business.pinterest.com/pinterest-business-partners/
    name: Work with Approved Pinterest Partners | Pinterest Business
    type: Partners
    description: 'null'
  - url: https://example.com/plans
    data:
      - id: trial
        name: Trial
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Trial tier.
        description: The temporary access.
      - id: standard
        name: Standard
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Standard tier.
        description: The standard access.
    name: Plans
    type: Plans
  - name: Rate Limits
    type: RateLimits
    description: The rate limits for this API.
    url: https://developers.pinterest.com/docs/reference/rate-limits/
    data:
      - name: Ads Analytics
        description: Fetching analytical data about ads.
        type: ads_analytics
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Ads Analytics
        description: Fetching analytical data about ads.
        type: ads_analytics
        tier: Standard
        limit: 300
        metric: request
        timeframe: minute
      - name: Ads Conversions
        description: Sending batches of conversion events for an ad account. This category applies to requests authenticated with a token acquired through the standard OAuth flow.
        type: ads_conversions
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Ads Conversions
        description: Sending batches of conversion events for an ad account. This category applies to requests authenticated with a token acquired through the standard OAuth flow.
        type: ads_conversions
        tier: Standard
        limit: 120000
        metric: request
        timeframe: minute
      - name: Ads Read
        description: Fetching information on ads, ad groups, ad campaigns or ad accounts.
        type: ads_read
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Ads Read
        description: Fetching information on ads, ad groups, ad campaigns or ad accounts.
        type: ads_read
        tier: Standard
        limit: 120000
        metric: request
        timeframe: minute
      - name: Ads Write
        description: Creating, editing or deleting ad entities, such as ad accounts, ads, ad groups or campaigns.
        type: ads_write
        tier: Trial
        limit: 300
        metric: request
        timeframe: day
      - name: Ads Write
        description: Creating, editing or deleting ad entities, such as ad accounts, ads, ad groups or campaigns.
        type: ads_write
        tier: Standard
        limit: 400
        metric: request
        timeframe: minute
      - name: Advanced Auction Read
        description: Fetching information related to bid options for ads auctions.
        type: advanced_auction_read
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Advanced Auction Read
        description: Fetching information related to bid options for ads auctions.
        type: advanced_auction_read
        tier: Standard
        limit: 50
        metric: request
        timeframe: minute
      - name: Advanced Auction Write
        description: Operating on ad auction bid items.
        type: advanced_auction_write
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Advanced Auction Write
        description: Operating on ad auction bid items.
        type: advanced_auction_write
        tier: Standard
        limit: 25
        metric: request
        timeframe: minute
      - name: Catalog Read
        description: Fetching item information from catalogs.
        type: catalogs_read
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Catalog Read
        description: Fetching item information from catalogs,
        type: catalogs_read
        tier: Standard
        limit: 100
        metric: request
        timeframe: minute
      - name: Catalog Write
        description: Creating or modifing item information for catalogs.
        type: catalogs_write
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Catalog Write
        description: Creating or modifing item information for catalogs.
        type: catalogs_write
        tier: Standard
        limit: 100
        metric: request
        timeframe: minute
      - name: Org Analytics
        description: Fetching user-related analytics data, such as account information and top Pins.
        type: org_analytics
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Org Analytics
        description: Fetching user-related analytics data, such as account information and top Pins.
        type: org_analytics
        tier: Standard
        limit: 60
        metric: request
        timeframe: minute
      - name: Org Read
        description: Fetching user accounts, boards, board sections, or Pins.
        type: org_read
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Org Read
        description: Fetching user accounts, boards, board sections, or Pins.
        type: org_read
        tier: Standard
        limit: 1000
        metric: request
        timeframe: minute
      - name: Org Write
        description: Creating, editing or deleting boards, board sections or Pins.
        type: org_write
        tier: Trial
        limit: 300
        metric: request
        timeframe: day
      - name: Org Write
        description: Creating, editing or deleting boards, board sections or Pins.
        type: org_write
        tier: Standard
        limit: 100
        metric: request
        timeframe: minute
      - name: Trends Read
        description: Fetching trending keyword information.
        type: trends_read
        tier: Trial
        limit: 1000
        metric: request
        timeframe: day
      - name: Trends Read
        description: Fetching trending keyword information.
        type: trends_read
        tier: Standard
        limit: 60
        metric: request
        timeframe: minute
  - name: OAuth Scopes
    type: OAuthScopes
    description: You must request at least one scope during the OAuth flow. You should only request the scopes required for your product.
    url: https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/#available-scopes
    data:
      - id: read_permissions
        name: Ads
        type: read
        description: See all data related to advertising, such as ads, ad groups and campaigns.
      - id: write_permissions
        name: Ads
        type: write
        description: Create, update or delete ads, ad groups and campaigns.
      - id: billing
        name: Billing
        type: read
        description: See all of your billing data, such as your billing profile.
      - id: billing
        name: Billing
        type: write
        description: Create, update or delete billing data.
      - id: biz_access
        name: Business Access
        type: read
        description: See all business access data.
      - id: biz_access
        name: Business Access
        type: write
        description: Create, update or delete business access data.
      - id: boards
        name: Boards
        type: read
        description: See public boards, including group boards, with boards read.
      - id: boards
        name: Boards
        type: read_secret
        description: See secret boards with boards read_secret.
      - id: boards
        name: Boards
        type: write
        description: Create, update or delete public boards with boards write.
      - id: boards
        name: Boards
        type: write_secret
        description: Create, update or delete secret boards with boards write_secret.
      - id: catalogs
        name: Catalogs
        type: read
        description: See all catalog data.
      - id: catalogs
        name: Catalogs
        type: write
        description: Create, update or delete catalogs.
      - id: pins
        name: Pins
        type: read
        description: See public pins with pins read.
      - id: pins
        name: Pins
        type: read_secret
        description: See secret pins with pins read_secret.
      - id: pins
        name: Pins
        type: write
        description: Create, update or delete public pins with pins write.
      - id: pins
        name: Pins
        type: write_secret
        description: Create, update or delete secret pins with pins write_secret.
      - id: user_accounts
        name: User Accounts
        type: read
        description: See user accounts and followers.
      - id: user_accounts
        name: User Accounts
        type: write
        description: Update user accounts and followers.
created: '2023-11-23'
modified: '2026-05-04'
position: Consuming
description: Pinterest is an American image sharing and social media service designed to enable saving and discovery of information like recipes, home, style, motivation, and inspiration on the internet using images and, on a smaller scale, animated GIFs and videos, in the form of pinboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.18'
---
