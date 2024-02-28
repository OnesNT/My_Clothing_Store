# My_Clothing_Store
"My Clothing Store" is a web application that provides a platform for users to explore and purchase a variety of clothing items. The application aims to offer a seamless shopping experience by showcasing a wide range of clothing products, providing detailed information about each item, and facilitating secure online transactions.

Description:

"My Clothing Store" is a web application that provides a platform for users to explore and purchase a variety of clothing items. The application aims to offer a seamless shopping experience by showcasing a wide range of clothing products, providing detailed information about each item, and facilitating secure online transactions.

Key Features:
User Registration and Authentication: Users can create accounts on the platform, allowing them to sign in securely and access personalized features such as order history and saved preferences.

Browsing and Shopping: The application offers a user-friendly interface for browsing through a diverse collection of clothing items. Users can explore products categorized by brand, category, color, and price range.

Product Details: Each clothing item is accompanied by detailed information, including the brand, category, color, price, and available sizes. Users can view high-quality images and descriptions to make informed purchasing decisions.

Shopping Cart: Users can add desired items to their shopping cart, review their selections, and proceed to checkout. The shopping cart functionality allows for easy management of selected items before making a purchase.

Secure Checkout: The application ensures secure payment processing by integrating with trusted payment gateways. Users can safely complete transactions using credit/debit cards or other supported payment methods.

User Account Management: Registered users have access to account management features, including profile editing, order tracking, and subscription management for promotional updates.

Responsive Design: The application is designed to be responsive across devices, ensuring a consistent and enjoyable shopping experience on desktops, laptops, tablets, and smartphones.

Future Enhancements:

Recommendation Engine: Implement personalized product recommendations based on user preferences and browsing history.
Social Integration: Allow users to share their favorite products on social media platforms and engage with the community.
Inventory Management: Integrate inventory management features to track stock levels, manage product availability, and receive alerts for low inventory items.
Localization: Support multiple languages and currencies to cater to a global audience.
Customer Support: Implement live chat support or ticketing system to assist users with inquiries, feedback, and support requests.
Technologies Used:

Frontend: HTML, CSS, JavaScript, Bootstrap
Backend: Python, Flask
Database: SQLite (or PostgreSQL, MySQL)
ORM: SQLAlchemy
Version Control: Git, GitHub

Target Audience:

The target audience for "My Clothing Store" includes fashion enthusiasts, shoppers looking for trendy and stylish clothing options, and individuals seeking a convenient and enjoyable online shopping experience.

Purpose:

The purpose of "My Clothing Store" is to provide a comprehensive and user-friendly platform for purchasing clothing items online. By offering a diverse selection of products, detailed product information, and secure payment options, the application aims to satisfy the fashion needs of its users and enhance their overall shopping experience.

### Physical Model

## Customer
| Title | Description | Data type | Restriction | PC | FK |
|-----------| ------------ | ------------|----------- | ------------| ------------|
| customer_id | Unique user ID | Bigserial| Not Null, Unique | + | |
| customer_nm | Real username | Varchar(40) | Not Null | | |
| customer_surname | User's real last name | Varchar(40) | Not Null | | |
| customer_patronymic | User's real middle name| Varchar(40) | | | |
| birth_dt | User date of birth | date | | | |
| email | Email address of the user | Varchar(50) | Not Null | | |
| overall_transactions_amt | The total price of purchased goods | bigint | | | |
| advertising_subscribe_flg | Flag indicating whether the user is subscribed to the promotional mailing list | Boolean | | ||


## Order
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| order_id | Unique Order ID | Bigserial| Not Null, Unique | + | |
| employee_id | Unique identifier of the employee who issued the order | BigInt | Not Null,>0 | | Employee|
| store_id | The unique ID of the store where the purchase was made | BigInt | Not Null,>0 | | Store|
| customer_id | Unique identifier of the buyer who made the order| BigInt | Not Null,>0 | |Customer|
| delivery_dttm | Date and time of delivery to the point of issue of the order | timestamp | | | |
| purchase_dtm | Date and time of redemption of the order from the point of issue | timestamp | | | |

## Clothes in order
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| order_id | The unique ID of the order that contains this item | Big serial | Not Null | + | Store|
| clothes_id | The unique identifier of the item that is in the order | Big serial | Not Null | + | clothes|
| item_count | The number of such things in this order | int | Not Null | | |

## Employee
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| employee_id | Unique employee ID | Bigserial| Not Null, Unique | + | |
| valid_from_dttm | Date from which the position is held | timestamp | Not Null | + | |
| delivery_point_id | The unique identifier of the pickup point where the employee works| BigInt | Not Null,>0 | | Delivery Point |
| employee_nm | Employee name | Varchar(40) | Not Null | | |
| employee_surname | Employee last name | Varchar(40) | Not Null | | |
| employee_patronymic | Middle name of the employee| Varchar(40) | | | |
| valid_to_dttm | Date before which the position was held | timestamp | Not Null | | |
| birth_dt | Employee's date of birth | date | Not Null | | |
| email | Email address of the employee | Varchar(50) | Not Null | | |
| salary_amt | Employee salary | int | | | |
| position_nm | Job title | Varchar(100) | Not Null| | |


## Delivery Point
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| delivery_point_id | Unique identifier of the point of issue | Big serial | Not Null, Unique | + | |
| store_id | The unique identifier of the store to which the pickup point belongs | BigInt | Not Null, >0 | | Store|
| address | Pickup point address | Varchar(40) | | | |
| city | City where the point of issue is located| Varchar(40) | | | |
| phone_no | Phone number of delivery point | int | | | |


## Store
| Title | Description | Data type | Restriction | PC | FK |
|-----------| ------------ | ------------|----------- | ------------| ------------|
| store_id | Shop Unique ID | Bigserial| Not Null, Unique | + | |
| store_nm | Store name | Varchar(60) | Not Null | | |
| create_dt | Store creation date | date | | | |
| head_office_address | Address where the main office is located | Varchar(40) | | | |
| head_office_country_nm | Country where head office is located| Varchar(40) | | | |

## Clothes in store
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| store_id | The unique ID of the store that has this item | Big serial | Not Null | + | Store|
| clothes_id | The unique identifier of the item that is in the store | Big serial | Not Null | + | clothes|
| item_count | The number of such things in this store | int | Not Null | | |

## Clothes
| Title | Description | Data type | Restriction | PC | FK |
|-----------| --------| ------------|----------- | ------------| ------------|
| clothes_id | Item Unique Identifier| Bigserial| Not Null, Unique | + | |
| brand_id | The unique identifier for the brand that released this item| BigInt | Not Null,>0 | | Brand|
| clothes_nm | Item name | Varchar(100) | Not Null | | |
| category_nm | Category of clothing to which the item belongs | Varchar(40) | Not Null | | |
| color_nm | Item color name| Varchar(40) | | | |
| price_amt | Cost | int | Not Null | | |
| sex_nm | The sex for which it was made | Varchar(50) | | | |

## Brand
| Title | Description | Data type | Restriction | PC | FK |
|-----------| ------------ | ------------|----------- | ------------| ------------|
| brand_id | Brand Unique Identifier | Bigserial| Not Null, Unique | + | |
| brand_nm | Brand name | Varchar(40) | Not Null | | |
| head_designer_nm | Name of chief designer| Varchar(40) | Not Null | | |
| head_designer_surname | Surname of the chief designer| Varchar(40) |Not Null | | |
| head_designer_patronymic | Middle name of the chief designer| Varchar(40) | | | |
| foundation_dt | Brand foundation date | Date | | | |

