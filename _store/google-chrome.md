---
aid: google-chrome
name: Google Chrome
description: Collection of APIs and resources for the Google Chrome browser and Chrome platform.
image: https://www.google.com/chrome/static/images/chrome-logo.svg
url: https://www.google.com/chrome/
type: Index
specificationVersion: '0.19'
tags:
  - Browser
  - Chrome Extensions
  - Developer Tools
  - Web Platform
created: '2024'
modified: '2026-04-18'
apis:
  - name: Chrome Extensions API
    description: APIs for building Chrome browser extensions.
    image: https://www.google.com/chrome/static/images/chrome-logo.svg
    humanUrl: https://developer.chrome.com/docs/extensions/
    baseUrl: chrome://extensions/
    tags:
      - Add-Ons
      - Browser
      - Extensions
    properties:
      - type: Documentation
        url: https://developer.chrome.com/docs/extensions/reference/
      - type: GettingStarted
        url: https://developer.chrome.com/docs/extensions/mv3/getstarted/
      - type: CodeExamples
        url: https://github.com/GoogleChrome/chrome-extensions-samples
      - type: APIReference
        url: https://developer.chrome.com/docs/extensions/reference/api
      - type: APIReference
        url: https://developer.chrome.com/docs/extensions/reference
      - type: Documentation
        url: https://developer.chrome.com/docs/extensions/develop/migrate
    contact:
      - type: Support
        url: https://support.google.com/chrome/
  - name: Chrome DevTools Protocol
    description: Instrument, inspect, debug and profile Chromium, Chrome and other Blink-based browsers.
    humanUrl: https://chromedevtools.github.io/devtools-protocol/
    baseUrl: ws://localhost:9222/devtools/browser
    tags:
      - Automation
      - Debugging
      - DevTools
      - Testing
    properties:
      - type: Documentation
        url: https://chromedevtools.github.io/devtools-protocol/
      - type: APIReference
        url: https://chromedevtools.github.io/devtools-protocol/tot/
      - type: GitHubRepository
        url: https://github.com/ChromeDevTools/devtools-protocol
      - type: Resources
        url: https://github.com/ChromeDevTools/awesome-chrome-devtools
    contact:
      - type: GitHub Issues
        url: https://github.com/ChromeDevTools/devtools-protocol/issues
  - name: Chrome Web Store API
    description: API for publishing and managing extensions in the Chrome Web Store.
    humanUrl: https://developer.chrome.com/docs/webstore/
    baseUrl: https://www.googleapis.com/chromewebstore/v1.1/
    tags:
      - Distribution
      - Publishing
      - Web Store
    properties:
      - type: Documentation
        url: https://developer.chrome.com/docs/webstore/using_webstore_api/
      - type: APIReference
        url: https://developer.chrome.com/docs/webstore/webstore_api/items/
      - type: Console
        url: https://chrome.google.com/webstore/devconsole
      - type: Authentication
        url: https://developer.chrome.com/docs/webstore/using_webstore_api/#beforeyoubegin
      - type: APIReference
        url: https://developer.chrome.com/docs/webstore/api/reference/rest
      - type: Documentation
        url: https://developer.chrome.com/docs/webstore/using-api
      - type: Blog
        url: https://developer.chrome.com/blog/cws-api-v2
    contact:
      - type: Support
        url: https://support.google.com/chrome_webstore/
  - name: Chrome Management API
    description: API for managing Chrome browser and Chrome OS devices in enterprise environments.
    humanUrl: https://developers.google.com/chrome/management
    baseUrl: https://chromemanagement.googleapis.com/
    tags:
      - Administration
      - Device Management
      - Enterprise
    properties:
      - type: Documentation
        url: https://developers.google.com/chrome/management/reference/rest
      - type: OpenAPI
        url: openapi/google-chrome-management-api-openapi.json
      - type: APIReference
        url: https://developers.google.com/chrome/management/reference/rest/v1/customers.apps
      - type: Console
        url: https://admin.google.com/
      - type: Documentation
        url: https://developers.google.com/chrome/management/guides/telemetry_api
      - type: Documentation
        url: https://developers.google.com/chrome/management/guides/reports_api
      - type: CodeExamples
        url: https://developers.google.com/chrome/management/guides/samples_telemetryapi
      - type: CodeExamples
        url: https://developers.google.com/chrome/management/guides/samples_reportsapi
      - type: GitHubRepository
        url: https://github.com/google/ChromeBrowserEnterprise
    contact:
      - type: Support
        url: https://support.google.com/chrome/a/
  - name: Chrome User Experience Report API
    description: Access real-world user experience data for popular websites.
    humanUrl: https://developers.google.com/web/tools/chrome-user-experience-report
    baseUrl: https://chromeuxreport.googleapis.com/
    tags:
      - Analytics
      - Metrics
      - Performance
      - User Experience
    properties:
      - type: Documentation
        url: https://developers.google.com/web/tools/chrome-user-experience-report/api/reference
      - type: APIReference
        url: https://developers.google.com/web/tools/chrome-user-experience-report/api/reference/rest
      - type: Documentation
        url: https://developers.google.com/web/tools/chrome-user-experience-report/bigquery/getting-started
      - type: Resources
        url: https://developer.chrome.com/docs/crux/methodology/tools
    contact:
      - type: Support
        url: https://support.google.com/webmasters/
  - name: Chrome Policy API
    description: API for programmatically viewing and managing Chrome policies assigned to Organizational Units.
    humanUrl: https://developers.google.com/chrome/policy
    baseUrl: https://chromepolicy.googleapis.com/
    tags:
      - Administration
      - Chrome OS
      - Enterprise
      - Policies
    properties:
      - type: Documentation
        url: https://developers.google.com/chrome/policy
      - type: Documentation
        url: https://developers.google.com/chrome/policy/guides/overview
      - type: Documentation
        url: https://developers.google.com/chrome/policy/guides/policy-schemas
      - type: GettingStarted
        url: https://developers.google.com/chrome/policy/guides/setup
      - type: CodeExamples
        url: https://developers.google.com/chrome/policy/guides/samples
    contact:
      - type: Support
        url: https://support.google.com/chrome/a/
  - name: Chrome Verified Access API
    description: API to cryptographically verify that ChromeOS clients are genuine and conform to corporate policy.
    humanUrl: https://developers.google.com/chrome/verified-access
    baseUrl: https://verifiedaccess.googleapis.com/
    tags:
      - Chrome OS
      - Enterprise
      - Security
      - Verification
    properties:
      - type: Documentation
        url: https://developers.google.com/chrome/verified-access
      - type: Documentation
        url: https://developers.google.com/chrome/verified-access/developer-guide
      - type: Documentation
        url: https://developers.google.com/chrome/verified-access/overview
    contact:
      - type: Support
        url: https://support.google.com/chrome/a/
  - name: Google Safe Browsing API
    description: API to check URLs against Google lists of unsafe web resources including phishing and malware sites.
    humanUrl: https://developers.google.com/safe-browsing
    baseUrl: https://safebrowsing.googleapis.com/
    tags:
      - Malware
      - Phishing
      - Security
      - URL Checking
    properties:
      - type: Documentation
        url: https://developers.google.com/safe-browsing
      - type: APIReference
        url: https://developers.google.com/safe-browsing/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/safe-browsing/v4/get-started
      - type: Documentation
        url: https://developers.google.com/safe-browsing/v4/lookup-api
      - type: GitHubRepository
        url: https://github.com/google/safebrowsing
    contact:
      - type: Support
        url: https://safebrowsing.google.com/
  - name: PageSpeed Insights API
    description: API to measure web page performance and receive optimization suggestions using Lighthouse and CrUX data.
    humanUrl: https://developers.google.com/speed/docs/insights/v5/about
    baseUrl: https://pagespeedonline.googleapis.com/
    tags:
      - Analytics
      - Lighthouse
      - Optimization
      - Performance
    properties:
      - type: Documentation
        url: https://developers.google.com/speed/docs/insights/rest
      - type: APIReference
        url: https://developers.google.com/speed/docs/insights/v5/reference
      - type: GettingStarted
        url: https://developers.google.com/speed/docs/insights/v5/get-started
    contact:
      - type: Support
        url: https://support.google.com/webmasters/
  - name: Chrome Built-in AI APIs
    description: On-device AI APIs powered by Gemini Nano built into Chrome for text generation, summarization, translation, and more.
    humanUrl: https://developer.chrome.com/docs/ai/built-in
    baseUrl: chrome://flags/#optimization-guide-on-device-model
    tags:
      - AI
      - Gemini Nano
      - Machine Learning
      - On-Device AI
    properties:
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/built-in
      - type: APIReference
        url: https://developer.chrome.com/docs/ai/built-in-apis
      - type: GettingStarted
        url: https://developer.chrome.com/docs/ai/get-started
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/prompt-api
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/summarizer-api
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/writer-api
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/rewriter-api
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/language-detection
      - type: Documentation
        url: https://developer.chrome.com/docs/ai/proofreader-api
    contact:
      - type: Support
        url: https://developer.chrome.com/docs/ai/built-in
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
common:
  - type: DeveloperPortal
    url: https://developer.chrome.com/
  - type: Blog
    url: https://developer.chrome.com/blog/
  - type: GitHubOrganization
    url: https://github.com/GoogleChrome
  - type: X
    url: https://twitter.com/ChromiumDev
  - type: YouTube
    url: https://www.youtube.com/c/GoogleChromeDevelopers
  - type: TermsOfService
    url: https://developers.google.com/terms
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: ReleaseNotes
    url: https://developer.chrome.com/release-notes
  - type: ChangeLog
    url: https://developer.chrome.com/new
  - type: StatusPage
    url: https://chromestatus.com/
  - type: Documentation
    url: https://developer.chrome.com/origintrials/
  - type: Documentation
    url: https://developer.chrome.com/docs/web-platform/origin-trials
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/google-chrome-extension
  - type: Portal
    url: https://chromeenterprise.google/
  - type: Resources
    url: https://source.chromium.org/chromium
  - type: JSONSchema
    url: json-schema/google-chrome-extension-manifest-schema.json
  - type: JSONLD
    url: json-ld/google-chrome-context.jsonld
  - type: Features
    data:
      - Chrome Extensions Manifest V3 platform
      - Chrome DevTools Protocol for browser automation
      - Chrome Web Store publishing and management APIs
      - Enterprise device and policy management
      - Real user experience metrics (CrUX)
      - Safe Browsing URL threat detection
      - PageSpeed Insights performance analysis
      - Built-in AI APIs (Gemini Nano)
      - Verified Access for ChromeOS device attestation
  - type: UseCases
    data:
      - Building and publishing Chrome browser extensions
      - Automating browser testing and debugging
      - Managing Chrome enterprise deployments at scale
      - Monitoring web performance with real user metrics
      - Protecting users from phishing and malware URLs
      - Running on-device AI inference in the browser
      - Enforcing Chrome policies across organizational units
  - type: Integrations
    data:
      - Google Workspace Admin
      - Google Cloud
      - Puppeteer
      - Playwright
      - Selenium
      - BigQuery
      - Lighthouse
      - Google Search Console
---
