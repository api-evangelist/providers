---
aid: google-chrome
url: https://raw.githubusercontent.com/api-evangelist/google-chrome/refs/heads/main/apis.yml
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
  - type: Getting Started
    url: https://developer.chrome.com/docs/extensions/mv3/getstarted/
  - type: Samples
    url: https://github.com/GoogleChrome/chrome-extensions-samples
  - type: API Reference
    url: https://developer.chrome.com/docs/extensions/reference/api
  - type: Manifest Reference
    url: https://developer.chrome.com/docs/extensions/reference
  - type: MV3 Migration Guide
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
  - type: Protocol Viewer
    url: https://chromedevtools.github.io/devtools-protocol/tot/
  - type: GitHub
    url: https://github.com/ChromeDevTools/devtools-protocol
  - type: API Reference
    url: https://chromedevtools.github.io/devtools-protocol/tot/
  - type: Awesome Chrome DevTools
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
  - type: API Reference
    url: https://developer.chrome.com/docs/webstore/webstore_api/items/
  - type: Developer Dashboard
    url: https://chrome.google.com/webstore/devconsole
  - type: Authentication
    url: https://developer.chrome.com/docs/webstore/using_webstore_api/#beforeyoubegin
  - type: V2 API Reference
    url: https://developer.chrome.com/docs/webstore/api/reference/rest
  - type: V2 API Guide
    url: https://developer.chrome.com/docs/webstore/using-api
  - type: V2 Announcement
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
  - type: API Reference
    url: https://developers.google.com/chrome/management/reference/rest/v1/customers.apps
  - type: Admin Console
    url: https://admin.google.com/
  - type: Telemetry API Guide
    url: https://developers.google.com/chrome/management/guides/telemetry_api
  - type: Reports API Guide
    url: https://developers.google.com/chrome/management/guides/reports_api
  - type: Telemetry API Samples
    url: https://developers.google.com/chrome/management/guides/samples_telemetryapi
  - type: Reports API Samples
    url: https://developers.google.com/chrome/management/guides/samples_reportsapi
  - type: GitHub
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
  - type: API Reference
    url: https://developers.google.com/web/tools/chrome-user-experience-report/api/reference/rest
  - type: Dataset
    url: https://developers.google.com/web/tools/chrome-user-experience-report/bigquery/getting-started
  - type: CrUX Tools
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
  - type: API Overview
    url: https://developers.google.com/chrome/policy/guides/overview
  - type: Policy Schemas
    url: https://developers.google.com/chrome/policy/guides/policy-schemas
  - type: Setup Guide
    url: https://developers.google.com/chrome/policy/guides/setup
  - type: Samples
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
  - type: Developer Guide
    url: https://developers.google.com/chrome/verified-access/developer-guide
  - type: Overview
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
  - type: API Reference
    url: https://developers.google.com/safe-browsing/reference/rest
  - type: Getting Started
    url: https://developers.google.com/safe-browsing/v4/get-started
  - type: Lookup API
    url: https://developers.google.com/safe-browsing/v4/lookup-api
  - type: GitHub
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
  - type: API Reference
    url: https://developers.google.com/speed/docs/insights/v5/reference
  - type: Getting Started
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
  - type: API Overview
    url: https://developer.chrome.com/docs/ai/built-in-apis
  - type: Getting Started
    url: https://developer.chrome.com/docs/ai/get-started
  - type: Prompt API
    url: https://developer.chrome.com/docs/ai/prompt-api
  - type: Summarizer API
    url: https://developer.chrome.com/docs/ai/summarizer-api
  - type: Writer API
    url: https://developer.chrome.com/docs/ai/writer-api
  - type: Rewriter API
    url: https://developer.chrome.com/docs/ai/rewriter-api
  - type: Language Detection API
    url: https://developer.chrome.com/docs/ai/language-detection
  - type: Proofreader API
    url: https://developer.chrome.com/docs/ai/proofreader-api
  contact:
  - type: Support
    url: https://developer.chrome.com/docs/ai/built-in
name: Google Chrome
tags:
- Browser
- Chrome Extensions
- Developer Tools
- Web Platform
type: Contract
image: https://www.google.com/chrome/static/images/chrome-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and resources for the Google Chrome browser and Chrome platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

