---
api_count: 0
artifact_total: 0
created: '2026-07-27'
description: 'E.ON Next Energy Limited is the United Kingdom retail supply arm of the E.ON Group, formed after E.ON''s 2019 acquisition of npower and serving roughly five million British households and small businesses with electricity, gas, smart meters, solar, home batteries, heat pumps and EV charging tariffs. It sits at the retail end of the GB energy value chain — buying wholesale, settling through Elexon, reading SMETS2 smart meters over the licensed Smart DCC network, and billing the customer — and it runs its entire operation on Kraken, the API-first, GraphQL-based energy operating system licensed from Kraken Technologies (Octopus Energy Group), onto which 5.8 million customers were migrated between June 2020 and June 2022. Its API posture is the exact opposite of its platform''s reputation: the Kraken architecture underneath is API-first, but nothing is published outward. There is no developer portal, no API documentation, no OpenAPI, and no third-party route to a customer''s usage
  or billing data; developer.eonnext.com and docs.eonnext.com do not resolve, and api.eonnext.com answers every path with an unauthenticated AWS API Gateway 403 "Missing Authentication Token". Britain mandated the metering infrastructure, not the data right — E.ON Next is bound by the Smart Energy Code and the DCC, which is live and implemented, but no consumer data-portability mandate equivalent to Australia''s CDR or Ontario''s Green Button applies to it, and none of the open GB market data (NESO Carbon Intensity, Elexon BSC, DNO open-data portals) originates here. Consumer data is closed, market data is published by other parties, and this profile is identity-only by evidence.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: E.ON Next
nav: Providers
network: true
random_paper: 66
slug: eon-next
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Retail
- Kraken
- Solar
- EV Charging
---
