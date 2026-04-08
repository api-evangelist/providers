---
aid: google-analytics-4
url: https://raw.githubusercontent.com/api-evangelist/google-analytics-4/refs/heads/main/apis.yml
apis:
- aid: google-analytics-4:google-analytics-data-api
  name: Google Analytics Data API
  description: The Google Analytics Data API v1 provides programmatic methods to access report data in Google Analytics 4 (GA4) properties.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
  humanURL: https://developers.google.com/analytics/devguides/reporting/data/v1
  baseURL: https://analyticsdata.googleapis.com
  tags:
  - Data
  - Dimensions
  - Metrics
  - Reports
  properties:
  - type: OpenAPI
    url: https://analyticsdata.googleapis.com/$discovery/rest?version=v1beta
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/reporting/data/v1
  - type: Authentication
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/basics#authentication
  - type: Quickstart
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
  - type: Rate Limits
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas
- aid: google-analytics-4:google-analytics-admin-api
  name: Google Analytics Admin API
  description: The Google Analytics Admin API allows programmatic configuration of Google Analytics 4 properties and data streams.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
  humanURL: https://developers.google.com/analytics/devguides/config/admin/v1
  baseURL: https://analyticsadmin.googleapis.com
  tags:
  - Administration
  - Configuration
  - Data Streams
  - Properties
  properties:
  - type: OpenAPI
    url: https://analyticsadmin.googleapis.com/$discovery/rest?version=v1beta
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/config/admin/v1
  - type: Authentication
    url: https://developers.google.com/analytics/devguides/config/admin/v1/rest
  - type: Quickstart
    url: https://developers.google.com/analytics/devguides/config/admin/v1/quickstart-client-libraries
- aid: google-analytics-4:google-analytics-measurement-protocol
  name: Google Analytics Measurement Protocol
  description: The Measurement Protocol for Google Analytics 4 allows developers to send events directly to Google Analytics servers for web and app streams.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
  humanURL: https://developers.google.com/analytics/devguides/collection/protocol/ga4
  baseURL: https://www.google-analytics.com/mp/collect
  tags:
  - Data Collection
  - Events
  - Server-Side
  - Tracking
  properties:
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/collection/protocol/ga4
  - type: Reference
    url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference
  - type: Validation
    url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events
  - type: Events
    url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/sending-events
name: Google Analytics 4
tags:
- Analytics
- Data Collection
- Marketing
- Measurement
- Mobile Analytics
- Reporting
- Web Analytics
type: Contract
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Analytics 4 (GA4) is the latest generation of Analytics that collects event-based data from websites and apps. It provides intelligent insights and predictive analytics powered by machine learning.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

