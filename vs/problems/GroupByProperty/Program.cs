using System;
using System.Collections.Generic;
using System.Linq;

namespace GroupByProperty {
    enum ItemColor {
        RED     = 0,
        BLUE    = 1,
        GREEN   = 2
    }

    enum ItemModel {
        MODEL_A = 0,
        MODEL_B = 1
    }

    struct Item {
        public ItemColor Color { get; private set; }
        public ItemModel Model { get; private set; }
        public String Description { get; private set; }

        public Item(ItemColor color, ItemModel model, String description) {
            Color = color;
            Model = model;
            Description = description;
        }

        public override String ToString() {
            return String.Format(
                "<COLOR: {0} MODEL: {1} DESC: {2}>", Color, Model, Description
            );
        }
    }

    class Program {
        static List<Item> GroupBy_v1(List<Item> items) {
            Dictionary<String, List<Item>> groups = 
                new Dictionary<string, List<Item>>();

            foreach (Item item in items) {
                String hash =
                    String.Format("#{0}#{1}", item.Color, item.Model);

                if (!groups.ContainsKey(hash)) {
                    groups[hash] = new List<Item>();
                }
                groups[hash].Add(item);
            }
            return groups.Values.SelectMany(item => item).ToList();
        }

        static List<Item> GroupBy_v2(List<Item> items) {
            return items.GroupBy(
                item => String.Format("#{0}#{1}", item.Color, item.Model)
            ).SelectMany(g => g).ToList();
        }

        static void Main(string[] args) {
            List<Item> items = new List<Item> {
                new Item(ItemColor.BLUE,  ItemModel.MODEL_A, "item BA.1"),
                new Item(ItemColor.GREEN, ItemModel.MODEL_A, "item GA.1"),
                new Item(ItemColor.RED,   ItemModel.MODEL_A, "item RA.1"),
                new Item(ItemColor.GREEN, ItemModel.MODEL_B, "item GB.1"),
                new Item(ItemColor.GREEN, ItemModel.MODEL_B, "item GB.2"),
                new Item(ItemColor.RED,   ItemModel.MODEL_B, "item RB.1"),
                new Item(ItemColor.BLUE,  ItemModel.MODEL_B, "item BB.2"),
                new Item(ItemColor.GREEN, ItemModel.MODEL_A, "item GA.2"),
                new Item(ItemColor.RED,   ItemModel.MODEL_A, "item RA.2"),
                new Item(ItemColor.RED,   ItemModel.MODEL_B, "item RB.2"),
                new Item(ItemColor.BLUE,  ItemModel.MODEL_A, "item BA.2"),
                new Item(ItemColor.BLUE,  ItemModel.MODEL_B, "item BB.1"),
            };
            List<Item> groupedList;

            Console.WriteLine(
                "original\n\t" + String.Join("\n\t", items) + '\n'
            );

            groupedList = GroupBy_v1(items);
            Console.WriteLine(
                "v1\n\t" + String.Join("\n\t", groupedList) + '\n'
            );

            groupedList = GroupBy_v2(items);
            Console.WriteLine(
                "v2\n\t" + String.Join("\n\t", groupedList) + '\n'
            );
        }
    }
}
