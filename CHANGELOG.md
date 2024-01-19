# Changelog

## [0.1.23](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.22...v0.1.23) (2024-01-19)


### Bug Fixes

* add 'generic' app to INSTALLED_APPS ([6e2d382](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6e2d3820ce7fc2051184c78e9065213e53e27fab))

## [0.1.22](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.21...v0.1.22) (2023-12-20)


### Bug Fixes

* set drf DEFAULT_PERMISSION_CLASSES to model permission ([91c4457](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/91c4457dbd0e4c54cd09b5c2c2510db5adb508ff))
* TEMPLATES: remove apis_ontology/templates from DIRS ([e7945e0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/e7945e07bdf2865d1708ca0fedc627b18be7bb18))
* use random secret key instead of hardcoding it ([0f7e9e3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/0f7e9e3d760104596c1f3b1bca950817c8ef1cce)), closes [#65](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/65)

## [0.1.21](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.20...v0.1.21) (2023-12-19)


### Bug Fixes

* typo in ROOT_URLCONF ([9840a10](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/9840a10c6c7097ec9c18f51d8a34f8e0d5515aa8))

## [0.1.20](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.19...v0.1.20) (2023-12-19)


### Bug Fixes

* bump default template pack for crispy ([9d8a3cb](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/9d8a3cb6450640e8b8a9a97bc634bbbc7ff94249))

## [0.1.19](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.18...v0.1.19) (2023-12-19)


### Bug Fixes

* add crispy_bootstrap4 to list of installed apps ([11f7300](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/11f7300294f3e4d9c2621318a1154fd70901a701))
* drop apis_labels from installed apps ([5c9a086](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/5c9a0864e5c3daac1d143b61312e057fc20c00f6))

## [0.1.18](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.17...v0.1.18) (2023-12-13)


### Bug Fixes

* drop deprecated context_processors ([ca114f3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ca114f3b08163d77b23ed146d82712248930c3f9)), closes [#55](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/55)

## [0.1.17](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.16...v0.1.17) (2023-12-11)


### Bug Fixes

* drop django-cors-headers related settings ([6620c56](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6620c5612b238d8ee024b45101e852cdf8defdfe))

## [0.1.16](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.15...v0.1.16) (2023-11-30)


### Bug Fixes

* drop deprecated context_processors ([7aa4ce6](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7aa4ce64ffd211552f21688324a4abedc74e485c))
* set ROOT_URLCONF to correct module ([2afd483](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/2afd483fb4dbafb26626ade3149c3ed6e86b9bb2))

## [0.1.15](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.14...v0.1.15) (2023-11-29)


### Bug Fixes

* get `ALLOWED_HOSTS` from `PUBLIC_URL` ([443b0c2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/443b0c267e57b505832a0be8c962dba148792372)), closes [#28](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/28)

## [0.1.14](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.13...v0.1.14) (2023-11-29)


### Bug Fixes

* add initial README ([ad64d78](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ad64d780830379cc4fbfee40f5f2096cab18b7a2))

## [0.1.13](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.12...v0.1.13) (2023-11-29)


### Bug Fixes

* provide default database setup ([911c0ec](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/911c0ec32908540aad65b85f9db2427556ff1da1)), closes [#33](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/33)

## [0.1.12](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.11...v0.1.12) (2023-11-28)


### Bug Fixes

* drop apis-override-select2js from dependencies ([0f7840f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/0f7840f6b7657f3cc2b2f7df32a1d9992a233892))

## [0.1.11](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.10...v0.1.11) (2023-11-24)


### Bug Fixes

* disable sentry tracing ([aa7c401](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/aa7c4019ca72938ad51254c2ff723696c03d4eef))

## [0.1.10](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.9...v0.1.10) (2023-10-19)


### Bug Fixes

* include ALLOWED_CIDR_NETS into settings ([dcbcfb8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/dcbcfb8bd1c5c3254fc0c3a936e6e1bf11a968cb)), closes [#19](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/19)

## [0.1.9](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.8...v0.1.9) (2023-10-18)


### Bug Fixes

* drop charts dependency ([d9ccb0f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d9ccb0f7d064dbbb92b36c7abea4761e42036c3b))
* drop WSGI_APPLICATION ([28aff2a](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/28aff2aa5e21b4b332bbfb7c95c4d54676724edf)), closes [#24](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/24)

## [0.1.8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.7...v0.1.8) (2023-10-05)


### Bug Fixes

* add apis_core.core to installed apps ([7d65db9](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7d65db9a5a09c5607d79a3bfcab69c977c054fbf))

## [0.1.7](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.6...v0.1.7) (2023-09-13)


### Bug Fixes

* remove the list view template override ([234ab87](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/234ab877f09a92e2e2bb9c2537e14ab30ee0d5f7))

## [0.1.6](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.5...v0.1.6) (2023-09-01)


### Bug Fixes

* drop ACDH_IMPRINT_URL ([1f43725](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1f437257aa32496ce9af81311339dab5f5b15441))

## [0.1.5](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.4...v0.1.5) (2023-08-23)


### Bug Fixes

* drop override of default templates ([f9fea45](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/f9fea45713bd9fe8f687c0afc8c6d3b88775cb8e))

## [0.1.4](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.3...v0.1.4) (2023-08-23)


### Bug Fixes

* drop webpage ([71dc49d](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/71dc49d7ff3b02bfb642967ea5fa042d945fd439))

## [0.1.3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.2...v0.1.3) (2023-08-21)


### Bug Fixes

* drop guardian settings ([167531e](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/167531e619d1ec0f429e35f342cba272404c377c))

## [0.1.2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.1...v0.1.2) (2023-08-18)


### Bug Fixes

* **deps:** add whitenoise dependency ([d5c43ce](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d5c43ceed7ab71cc725b56e4d5f6c05886121d6f)), closes [#3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/3)
* **deps:** loosen Python dependency version constraints ([56cf49f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/56cf49f0fc53b74ebbf6d1057c3876184f3b96b6))

## [0.1.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.0...v0.1.1) (2023-08-16)


### Bug Fixes

* **deps:** add apis-override-select2js to the dependencies ([422f8e2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/422f8e2e948cbeee7bdb4f64a0735f9204eb5136))

## 0.1.0 (2023-08-16)


### Bug Fixes

* rename module folder to adhere to Python convention ([d9d873b](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d9d873b1b5decf53dcaa58cf4a0a95f6a2b3f944))
