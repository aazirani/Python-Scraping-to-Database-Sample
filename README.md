# Python Script for Scraping Data from a Website and Saving it to a Database
Some sample code examples in Python to scrape data from the web and saving it to a database.

This repository is the fully implemented code of the tutorial "[Step by Step Guide on Scraping Data from a Website and Saving it to a Database](https://howpcrules.com/step-by-step-guide-on-scraping-data-from-a-website-and-saving-it-to-a-database/)" on [howpcrules.com](https://howpcrules.com/). For a more detailed tutorial please take a look at the blog post.

Web scraping and saving data to a database is the goal of this piece of code and the sample page being scraped is the following:  [https://howpcrules.com/sample-page-for-web-scraping/](https://howpcrules.com/sample-page-for-web-scraping/).
## Requirements
1. A working version of Python 2 or Python 3.
2. Locally running MySQL software.
3. Python libraries beautifulsoup4, MySQLdb aka. mysqlclient and requests.
4. An active internet connection.

## Quick Start
1. Open your locally run MySQL software (phpMyAdmin, Sequel Pro etc.) and create a database with the name "scraping_sample".
2. Create a user with the username "scraping_user" and give the user the needed privileges to read and modify the table "scraping_sample".
3. Navigate to the MySQL command line and execute the following commands to create the needed tables to save the scraped data into.
```sql
CREATE TABLE `classes` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `name_of_class` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `type_of_course` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `number` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `short_text` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `choice_term` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `hours_per_week_in_term` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `expected_num_of_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `maximum_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `assignment` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `lecture_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `credit_points` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `hyperlink` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `language` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `events` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `class_id` int(10) unsigned NOT NULL,
 `start_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `day` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `start_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `frequency` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `room` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer_for_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `remarks` text COLLATE utf8_unicode_ci,
 `cancelled_on` text COLLATE utf8_unicode_ci,
 `max_participants` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`),
 KEY `events_class_id_foreign` (`class_id`),
 CONSTRAINT `events_class_id_cascade` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```
4. Clone this repository into a folder
5. Go to the just cloned folder and execute the script
For Python 3:
```
python3 scraping_single_web_page.py
```
For Python 2:
```
python2 scraping_single_web_page.py
```