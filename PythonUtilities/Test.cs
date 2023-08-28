//filename: test.csx

for (int index = 0; index < 10; index++)
{
    Console.WriteLine($"Sample Value {index}");
}

List<string> list = new List<string>();

for (int index = 0; index < 10; index++)
{
    list.Add($"List Index {index}");
}

Console.WriteLine();
Console.WriteLine("--------------------------");
Console.WriteLine();

foreach (string item in list)
{
    Console.WriteLine(item);
}