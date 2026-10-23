# -*- coding: utf-8 -*-
"""
Smart Grocery Tracker v4.2 (Bilingual & Bug-Free)
Author: You
Description: A CLI app for tracking groceries with auto-unit detection and FA/EN support.
"""

import sys

# ---------------------------------------------------------
# 1. Localization Dictionary (All UI Texts Here)
# ---------------------------------------------------------
LANG_CONFIG = {
    'fa': {
        'title': "   سیستم مدیریت خرید هوشمند v4.2",
        'menu_add': "1. افزودن کالاها",
        'menu_view': "2. مشاهده فاکتور",
        'menu_clear': "3. خالی کردن سبد",
        'menu_exit': "4. خروج",
        'prompt_choice': "انتخاب شما (1-4): ",
        'invalid_option': "⚠️ گزینه نامعتبر.",
        
        # Input Flow
        'ask_count': "\n🔢 چند قلم کالا می‌خواهید اضافه کنید؟ ",
        'cancel_msg': "⚠️ عملیات لغو شد.",
        'positive_num_err': "⚠️ تعداد باید عدد مثبت باشد.",
        'int_err': "❌ لطفاً عدد صحیح وارد کنید.",
        'header_enter': "\n--- شروع ورود اطلاعات ---\n--- (برای توقف زودهنگام، نام کالا را خالی بگذارید) ---\n",
        'item_counter': "[درخواست {} از {}]",
        'ask_name': "   نام کالا (یا Enter برای پایان): ",
        'stop_input': "\nℹ️ ورود متوقف شد.",
        'detected_unit': "   🤖 تشخیص داده شد: '{}' با واحد [{}] معامله می‌شود.",
        'unknown_item': "   ❓ کالای '{}' در لیست نیست.",
        'select_unit_header': "   واحد اندازه‌گیری را انتخاب کنید:",
        'unit_kg': "   1. کیلوگرم (kg)",
        'unit_g': "   2. گرم (g)",
        'unit_l': "   3. لیتر (L)",
        'unit_ml': "   4. میلی‌لیتر (ml)",
        'unit_pcs': "   5. عدد (pcs)",
        'ask_unit_choice': "   انتخاب شما (1-5): ",
        'unit_set': "   ✅ واحد تنظیم شد: {}",
        'ask_qty': "   مقدار مورد نظر ({}) چقدر است؟ ", 
        'qty_pos_err': "   ⚠️ مقدار باید بیشتر از صفر باشد.",
        'qty_int_err': "   ❌ لطفاً عدد وارد کنید.",
        'ask_price': "   قیمت هر {} (تومان): ",
        'price_neg_err': "   ⚠️ قیمت نمی‌تواند منفی باشد.",
        'price_int_err': "   ❌ لطفاً عدد وارد کنید.",
        'item_added': "   ✅ ثبت شد. هزینه این بخش: {:,.0f} تومان\n",
        'no_items_added': "❌ هیچ کالایی ثبت نشد.",
        'items_added_success': "📦 {} کالا به سبد اضافه شد.",
        
        # Receipt
        'receipt_title': "           🧾 فاکتور هوشمند خرید شما",
        'empty_cart': "\n🛒 سبد خالی است!",
        'th_no': "ردیف",
        'th_name': "نام کالا",
        'th_qty': "خرید",
        'th_unit': "واحد",
        'th_price': "قیمت واحد",
        'th_total': "جمع کل",
        'grand_total_label': "مجموع کل پرداختی (تومان):",
        'note_standard_units': "💡 نکته: قیمت‌ها بر اساس واحد استاندارد محاسبه شده‌اند.",
        'calc_complete': "✅ حساب و کتاب تمام شد.\n",
        
        # Clear
        'confirm_clear': "\nآیا مطمئنید که می‌خواهید سبد را خالی کنید؟ (y/n): ",
        'cart_cleared': "🗑️ سبد پاک شد.",
        'action_cancelled': "✅ لغو شد.",
        
        # Exit
        'goodbye': "👋 خداحافظ!"
    },
    'en': {
        'title': "   Smart Grocery Tracker v4.2",
        'menu_add': "1. Add Items",
        'menu_view': "2. View Receipt",
        'menu_clear': "3. Clear Cart",
        'menu_exit': "4. Exit",
        'prompt_choice': "Select option (1-4): ",
        'invalid_option': "⚠️ Invalid option.",
        
        # Input Flow
        'ask_count': "\n🔢 How many items do you want to add? ",
        'cancel_msg': "⚠️ Operation cancelled.",
        'positive_num_err': "⚠️ Number must be positive.",
        'int_err': "❌ Please enter a valid integer.",
        'header_enter': "\n--- Start Entering Details ---\n--- (Press Enter without name to stop early) ---\n",
        'item_counter': "[Item {} of {}]",
        'ask_name': "   Item Name (or Enter to skip): ",
        'stop_input': "\nℹ️ Input stopped by user.",
        'detected_unit': "   🤖 Detected: '{}' is sold per [{}].",
        'unknown_item': "   ❓ Unknown item: '{}'. Select unit manually:",
        'select_unit_header': "   Select Measurement Unit:",
        'unit_kg': "   1. Kilograms (kg)",
        'unit_g': "   2. Grams (g)",
        'unit_l': "   3. Liters (L)",
        'unit_ml': "   4. Milliliters (ml)",
        'unit_pcs': "   5. Pieces (pcs)",
        'ask_unit_choice': "   Your choice (1-5): ",
        'unit_set': "   ✅ Unit set to: {}",
        'ask_qty': "   How much {} do you need? ", 
        'qty_pos_err': "   ⚠️ Quantity must be greater than zero.",
        'qty_int_err': "   ❌ Invalid number. Try again.",
        'ask_price': "   Price per {} ($): ",
        'price_neg_err': "   ⚠️ Price cannot be negative.",
        'price_int_err': "   ❌ Invalid number. Try again.",
        'item_added': "   ✅ Added. Estimated Cost: ${:,.2f}\n",
        'no_items_added': "❌ No items were added.",
        'items_added_success': "📦 {} items successfully added to cart.",
        
        # Receipt
        'receipt_title': "           🧾 SMART GROCERY RECEIPT",
        'empty_cart': "\n🛒 Cart is empty!",
        'th_no': "No.",
        'th_name': "Item",
        'th_qty': "Qty",
        'th_unit': "Unit",
        'th_price': "Price/Unit",
        'th_total': "Total",
        'grand_total_label': "GRAND TOTAL:",
        'note_standard_units': "💡 Note: Prices are calculated based on standard units.",
        'calc_complete': "✅ Calculation complete.\n",
        
        # Clear
        'confirm_clear': "\nAre you sure you want to clear the entire cart? (y/n): ",
        'cart_cleared': "🗑️ Cart cleared successfully.",
        'action_cancelled': "✅ Action cancelled.",
        
        # Exit
        'goodbye': "👋 Goodbye! Happy Shopping."
    }
}

# ---------------------------------------------------------
# 2. Product Database
# ---------------------------------------------------------
PRODUCT_DB = {
    "شیر": {"unit": "L", "display_fa": "لیتر", "display_en": "Liter"},
    "milk": {"unit": "L", "display_fa": "لیتر", "display_en": "Liter"},
    
    "ماست": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "yogurt": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "پنیر": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "cheese": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "کره": {"unit": "g", "display_fa": "گرم", "display_en": "Gram"},
    "butter": {"unit": "g", "display_fa": "گرم", "display_en": "Gram"},
    
    "خامه": {"unit": "ml", "display_fa": "میلی‌لیتر", "display_en": "Milliliter"},
    "cream": {"unit": "ml", "display_fa": "میلی‌لیتر", "display_en": "Milliliter"},
    
    "تخم مرغ": {"unit": "pcs", "display_fa": "عدد", "display_en": "Piece"},
    "eggs": {"unit": "pcs", "display_fa": "عدد", "display_en": "Piece"},

    "برنج": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "rice": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "آرد": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "flour": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "شکر": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "sugar": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "روغن مایع": {"unit": "L", "display_fa": "لیتر", "display_en": "Liter"},
    "oil": {"unit": "L", "display_fa": "لیتر", "display_en": "Liter"},
    
    "رب گوجه": {"unit": "g", "display_fa": "گرم", "display_en": "Gram"},
    "tomato paste": {"unit": "g", "display_fa": "گرم", "display_en": "Gram"},

    "گوشت قرمز": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "beef": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "مرغ": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "chicken": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "ماهی": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "fish": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},

    "سیب": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "apple": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "پرتقال": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "orange": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "خیار": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "cucumber": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    
    "گوجه فرنگی": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
    "tomato": {"unit": "kg", "display_fa": "کیلوگرم", "display_en": "Kilogram"},
}

CONVERSION_FACTORS = {
    "kg": 1.0,
    "g": 0.001,
    "L": 1.0,
    "ml": 0.001,
    "pcs": 1.0
}

class GroceryTracker:
    def __init__(self):
        self.cart = []
        self.total_cost = 0.0
        self.lang = 'fa'  # Default language

    def set_language(self):
        print("\nPlease select your language / لطفا زبان خود را انتخاب کنید:")
        print("1. English")
        print("2. فارسی (Persian)")
        choice = input("Choice (1/2): ").strip()
        
        if choice == '1':
            self.lang = 'en'
            print("Language set to English.")
        else:
            self.lang = 'fa'
            print("زبان روی فارسی تنظیم شد.")
            
        return LANG_CONFIG[self.lang]

    def get_text(self, key):
        return LANG_CONFIG[self.lang][key]

    def find_product_unit(self, item_name):
        clean_name = item_name.strip().lower()
        
        # Exact match
        if clean_name in PRODUCT_DB:
            return PRODUCT_DB[clean_name]
        
        # Partial match
        for key, value in PRODUCT_DB.items():
            if key.lower() in clean_name or clean_name in key.lower():
                return value
                
        return None

    def add_items_batch(self):
        t = lambda k: self.get_text(k) 
        
        try:
            count_input = input(t('ask_count'))
            if not count_input.strip():
                print(t('cancel_msg'))
                return
            
            num_items = int(count_input)
            if num_items <= 0:
                print(t('positive_num_err'))
                return
        except ValueError:
            print(t('int_err'))
            return

        print(t('header_enter'))
        
        added_count = 0
        
        for i in range(num_items):
            counter_msg = t('item_counter').format(i+1, num_items)
            print(counter_msg)
            
            # 1. Get Name
            raw_name = input(t('ask_name')).strip()
            if not raw_name:
                print(t('stop_input'))
                break
            
            # 2. Detect Unit
            db_info = self.find_product_unit(raw_name)
            
            if db_info:
                std_unit = db_info["unit"]
                display_unit_key = f"display_{self.lang}"
                display_unit = db_info[display_unit_key]
                
                msg = t('detected_unit').format(raw_name, display_unit)
                print(msg)
            else:
                print(t('unknown_item').format(raw_name))
                print(t('select_unit_header'))
                print(t('unit_kg'))
                print(t('unit_g'))
                print(t('unit_l'))
                print(t('unit_ml'))
                print(t('unit_pcs'))
                
                u_choice = input(t('ask_unit_choice')).strip()
                mapping = {'1': 'kg', '2': 'g', '3': 'L', '4': 'ml', '5': 'pcs'}
                std_unit = mapping.get(u_choice, 'pcs')
                
                manual_labels = {
                    'fa': {'kg': 'کیلوگرم', 'g': 'گرم', 'L': 'لیتر', 'ml': 'میلی‌لیتر', 'pcs': 'عدد'},
                    'en': {'kg': 'Kilogram', 'g': 'Gram', 'L': 'Liter', 'ml': 'Milliliter', 'pcs': 'Piece'}
                }
                display_unit = manual_labels[self.lang][std_unit]
                print(t('unit_set').format(display_unit))

            # 3. GET QUANTITY
            while True:
                qty_prompt = t('ask_qty').format(display_unit)
                qty_str = input(qty_prompt).strip()
                try:
                    quantity = float(qty_str)
                    if quantity > 0:
                        break
                    else:
                        print(t('qty_pos_err'))
                except ValueError:
                    print(t('qty_int_err'))

            # 4. Get Price
            price_prompt = t('ask_price').format(display_unit)
                 
            while True:
                price_str = input(price_prompt).strip()
                try:
                    unit_price = float(price_str)
                    if unit_price >= 0:
                        break
                    else:
                        print(t('price_neg_err'))
                except ValueError:
                    print(t('price_int_err'))

            # 5. Calculate
            factor = CONVERSION_FACTORS[std_unit]
            base_quantity = quantity * factor 
            subtotal = base_quantity * unit_price
            
            cart_item = {
                "name": raw_name,
                "unit_code": std_unit,
                "unit_label": display_unit,
                "input_qty": quantity,
                "base_qty": base_quantity,
                "price_per_unit": unit_price,
                "subtotal": subtotal
            }
            
            self.cart.append(cart_item)
            added_count += 1
            
            print(t('item_added').format(subtotal))

        if added_count == 0:
            print(t('no_items_added'))
        else:
            print(t('items_added_success').format(added_count))
            self.show_receipt()

    def show_receipt(self):
        t = lambda k: self.get_text(k)
        
        if not self.cart:
            print(t('empty_cart'))
            return

        self.total_cost = sum(item['subtotal'] for item in self.cart)

        print("\n" + "="*65)
        print(t('receipt_title'))
        print("="*65)
        
        header = f"{t('th_no'):<4} | {t('th_name'):<15} | {t('th_qty'):>8} | {t('th_unit'):<10} | {t('th_price'):>10} | {t('th_total'):>10}"
        print(header)
        print("-"*65)
        
        for index, item in enumerate(self.cart, start=1):
            qty_fmt = f"{item['input_qty']:>8.2f}".rstrip('0').rstrip('.')
            
            if self.lang == 'fa':
                price_fmt = f"{item['price_per_unit']:>9,.0f}"
                sub_fmt = f"{item['subtotal']:>9,.0f}"
                total_fmt = f"{self.total_cost:>10,.0f}"
            else:
                price_fmt = f"${item['price_per_unit']:>9,.2f}"
                sub_fmt = f"${item['subtotal']:>9,.2f}"
                total_fmt = f"${self.total_cost:>10,.2f}"
            
            name_pad = f"{item['name']:<15}"
            unit_pad = f"{item['unit_label']:<10}"
            
            line = f"{index:<4} | {name_pad} | {qty_fmt} | {unit_pad} | {price_fmt} | {sub_fmt}"
            print(line)
            
        print("-"*65)
        print(f"{t('grand_total_label'):<45} {total_fmt}")
        print("="*65)
        print(t('note_standard_units'))
        print(t('calc_complete'))

    def clear_cart(self):
        t = lambda k: self.get_text(k)
        confirm = input(t('confirm_clear'))
        if confirm.lower() == 'y':
            self.cart.clear()
            self.total_cost = 0.0
            print(t('cart_cleared'))
        else:
            print(t('action_cancelled'))

def main():
    tracker = GroceryTracker()
    
    # 1. Select Language First
    tracker.set_language()
    t = lambda k: tracker.get_text(k)

    while True:
        print("\n" + "-"*40)
        print(t('title'))
        print("-"*40)
        print(t('menu_add'))
        print(t('menu_view'))
        print(t('menu_clear'))
        print(t('menu_exit'))
        
        choice = input(t('prompt_choice')).strip()

        if choice == '1':
            tracker.add_items_batch()
        elif choice == '2':
            tracker.show_receipt()
        elif choice == '3':
            tracker.clear_cart()
        elif choice == '4':
            print(t('goodbye'))
            break
        else:
            print(t('invalid_option'))

if __name__ == "__main__":
    main()