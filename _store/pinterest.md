---
aid: pinterest
url: >-
  https://raw.githubusercontent.com/api-search/images/main/_apis/pinterest/apis.md
apis:
  - aid: pinterest:pinterest-api
    name: Pinterest API
    tags:
      - Images
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.pinterest.com/
    properties:
      - url: https://developers.pinterest.com/docs/api/v5/
        type: Documentation
      - url: properties/pinterest-api-openapi.yml
        type: OpenAPI
    description: This is the description of your API.
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
  - url: properties/api-description
    name: OpenAPI
    type: OpenAPI
  - url: https://www.pintereststatus.com/
    name: Sttus
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
  - url: >-
      https://developers.pinterest.com/docs/api-features/track-conversion-events/
    name: Pinterest Developers
    type: Features
    description: 'null'
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
  - url: https://developers.pinterest.com/docs/reference/rate-limits/
    data:
      - name: Ads Analytics
        tier: Trial
        type: ads_analytics
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching analytical data about ads.
      - name: Ads Analytics
        tier: Standard
        type: ads_analytics
        limit: 300
        metric: request
        timeframe: minute
        description: Fetching analytical data about ads.
      - name: Ads Conversions
        tier: Trial
        type: ads_conversions
        limit: 1000
        metric: request
        timeframe: day
        description: >-
          Sending batches of conversion events for an ad account. This category
          applies to requests authenticated with a token acquired through the
          standard OAuth flow.
      - name: Ads Conversions
        tier: Standard
        type: ads_conversions
        limit: 120000
        metric: request
        timeframe: minute
        description: >-
          Sending batches of conversion events for an ad account. This category
          applies to requests authenticated with a token acquired through the
          standard OAuth flow.
      - name: Ads Read
        tier: Trial
        type: ads_read
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching information on ads, ad groups, ad campaigns or ad accounts.
      - name: Ads Read
        tier: Standard
        type: ads_read
        limit: 120000
        metric: request
        timeframe: minute
        description: Fetching information on ads, ad groups, ad campaigns or ad accounts.
      - name: Ads Write
        tier: Trial
        type: ads_write
        limit: 300
        metric: request
        timeframe: day
        description: >-
          Creating, editing or deleting ad entities, such as ad accounts, ads,
          ad groups or campaigns.
      - name: Ads Write
        tier: Standard
        type: ads_write
        limit: 400
        metric: request
        timeframe: minute
        description: >-
          Creating, editing or deleting ad entities, such as ad accounts, ads,
          ad groups or campaigns.
      - name: Advanced Auction Read
        tier: Trial
        type: advanced_auction_read
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching information related to bid options for ads auctions.
      - name: Advanced Auction Read
        tier: Standard
        type: advanced_auction_read
        limit: 50
        metric: request
        timeframe: minute
        description: Fetching information related to bid options for ads auctions.
      - name: Advanced Auction Write
        tier: Trial
        type: advanced_auction_write
        limit: 1000
        metric: request
        timeframe: day
        description: Operating on ad auction bid items.
      - name: Advanced Auction Write
        tier: Standard
        type: advanced_auction_write
        limit: 25
        metric: request
        timeframe: minute
        description: Operating on ad auction bid items.
      - name: Catalog Read
        tier: Trial
        type: catalogs_read
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching item information from catalogs.
      - name: Catalog Read
        tier: Standard
        type: catalogs_read
        limit: 100
        metric: request
        timeframe: minute
        description: Fetching item information from catalogs,
      - name: Catalog Write
        tier: Trial
        type: catalogs_write
        limit: 1000
        metric: request
        timeframe: day
        description: Creating or modifing item information for catalogs.
      - name: Catalog Write
        tier: Standard
        type: catalogs_write
        limit: 100
        metric: request
        timeframe: minute
        description: Creating or modifing item information for catalogs.
      - name: Org Analytics
        tier: Trial
        type: org_analytics
        limit: 1000
        metric: request
        timeframe: day
        description: >-
          Fetching user-related analytics data, such as account information and
          top Pins.
      - name: Org Analytics
        tier: Standard
        type: org_analytics
        limit: 60
        metric: request
        timeframe: minute
        description: >-
          Fetching user-related analytics data, such as account information and
          top Pins.
      - name: Org Read
        tier: Trial
        type: org_read
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching user accounts, boards, board sections, or Pins.
      - name: Org Read
        tier: Standard
        type: org_read
        limit: 1000
        metric: request
        timeframe: minute
        description: Fetching user accounts, boards, board sections, or Pins.
      - name: Org Write
        tier: Trial
        type: org_write
        limit: 300
        metric: request
        timeframe: day
        description: Creating, editing or deleting boards, board sections or Pins.
      - name: Org Write
        tier: Standard
        type: org_write
        limit: 100
        metric: request
        timeframe: minute
        description: Creating, editing or deleting boards, board sections or Pins.
      - name: Trends Read
        tier: Trial
        type: trends_read
        limit: 1000
        metric: request
        timeframe: day
        description: Fetching trending keyword information.
      - name: Trends Read
        tier: Standard
        type: trends_read
        limit: 60
        metric: request
        timeframe: minute
        description: Fetching trending keyword information.
    name: Rate Limits
    type: RateLimits
    description: The rate limits for this API.
  - url: >-
      https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/#available-scopes
    data:
      - id: read_permissions
        name: Ads
        type: read
        description: >-
          See all data related to advertising, such as ads, ad groups and
          campaigns.
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
    name: OAuth Scopes
    type: OAuthScopes
    description: >-
      You must request at least one scope during the OAuth flow. You should only
      request the scopes required for your product.
created: '2023-11-23'
modified: '2025-08-18'
position: Consuming
description: |-

  Pinterest is an American image sharing and social media service designed to
  enable saving and discovery of information like recipes, home, style,
  motivation, and inspiration on the internet using images and, on a smaller
  scale, animated GIFs and videos, in the form of pinboards.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---