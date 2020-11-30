
using System;
using System.Collections.Generic;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace Nigeria
{
    internal class Program
    {
        public static int playerHealth = 10;
        public static int monsterHealth = 1;
        public static bool iscombat = false;
        private static readonly string a = "slsd!#$sa";
        private static readonly string b = "#$KD213ks";
        private static readonly string c = "@13Ag1S4d3f6g123";
        public static Scene currentScene;
        public static List<Scene> scenes;

        private static void Main(string[] args)
        {
            Program.LoadGame(Program.getScenes());
        }

        public static void SaveGame()
        {
            File.WriteAllText("save", Program.Decrypt(Program.currentScene.uuid));
        }

        public static void LoadGame(Scene def)
        {
            if (File.Exists("save"))
            {
                string str = Program.Encrypt(File.ReadAllText("save"));
                bool flag = false;
                foreach (Scene scene in Program.scenes)
                {
                    if (str == scene.uuid)
                    {
                        flag = true;
                        scene.start();
                        break;
                    }
                }
                if (flag)
                    return;
                def.start();
            }
            else
                def.start();
        }

        public static Scene getScenes()
        {
            Program.scenes = new List<Scene>();
            Scene scene1 = new Scene("qA3vZskgFK/Y6HTWRSLdkjmCnzCCEEtECdBWoRsXvlefiCnuj0dZkLhIfwU187An", "YOB7pEKDTpmN9CHLue04M/7z5F0Ez6vSzl/s5cqoW3Hw7EY/M5YSV/ZCY/X//fvljIaMjWO6e2KT2nexMMHmNm5UDY48QxAI21x127R9gnnqUrjH35IFOuMEfn4p2w6aedETJ7i07KPKHbAwm/23pPmaGdLPj4JCXfGqwlRmh2vqpJjKlxmr41r4SwPkqJyK");
            Scene scene2 = new Scene("ToNZcyNSqEUFKFnasHguoxz1FUKsu1apzzyClm9ZIP92jli590fOTaL/fEWl6mjt", "YOB7pEKDTpmN9CHLue04M1mZGKFM7V +Tg6AS1VrausvKBmPTovFMoZdOmvzGrLvypBhKASrOZBpBxhOqvdrvQ5yeHgbuAjzbxdifePJWSGdsuEes2uhr3t6N8pte8YuIYeyTAbrT2NIpNip1jsHT2fsCQwF9KtHzfx5LfKeCFlM=");
            Scene scene3 = new Scene("9elLhaBqwpxGjW6bUG7wOjlGfOQPsF4MeqtTetPhf6GRfKe4Ix2mEi7ZHEonKbKE", "l9eHhIAACE4udS0rORoV +iT/f82VShTv7eVlXS0cEKO5HRtLoJJemJzlcQcQ4wb+");
            Scene scene4 = new Scene("kx3Np5vQOK2Ci6y2S9fQjSGXoiqFZtldm+1jMTJMw0u62AtHEsXrSV1mz4W+yneX", "cnw2cQ6DQLwdeU8SPh0FDk1Rg +S5qozmYlO3JBIwPcyDXNB7eixYG0TduUc2dmam//QAzHQwQKJNEDeWsVwGEA==");
            Scene scene5 = new Scene("EuZJN3jXIocVjgDhCVWMjqDjDArX0HB+VuVjkrWQTUvSrc7zWsRduOCNOnrwIqgF", "CW71dsAZllxYgp6QXsmBr /TzA1VK3c0SOuuI9/wK+oCJFd7lO594lYqK6qtsF/2XpfP5aEdbXlZqvIq/Zts1Dba1dKGs7I7HqJbFIDpKDzI=");
            Scene scene6 = new Scene("Ta6gpeWqN2Ak3+/0ZwxCNtkVyD8c6tdjhMLmnjJpNwakODgLz6sR1ZrMGyaDlYmC", "V9SL /BSaZYMGlfqAsUzOX47L6EtEemRDkEcloA90k5ONsJKbp3F/2qxUskXyhw13wh3WlK3khDiPK0uosHPhoVXJfbRayt2zN2Z8oqZXqieVItMyOekRMS0Gfw7rqfZx");
            Scene scene7 = new Scene("TJhmehq/zCEhL6KUf/h8bfO5PmdmyZLZ2SoUl9E9Wdo3wLnpWjNqphgOda1lagBQ", "OA3rtqBXCv7iYKesRbh6/rlmjJk/UHmHhTpv+u44Tlq9lwnahah6uXI5dnNcVvFc+b9l2QvKVl4zbhzWdoS+h+qp/lFpoLr1m7MxQC34oB4=");
            Scene scene1_1 = new Scene("RDdAsJvuC/i0kXrxWvwkmc2PG4BuLkzb1WYMQP1qfUmbQ7L2lFRn3RB3GAT3t21w", "N02yuDwAjOYGrIlPMo4MOh5HhINkqsk69XvUjVug2jUFBTYIvMNAYhAt+hLfSc2C");
            Scene scene8 = new Scene("mH98eAaEABRtE4Id2ZpW2A1oXbdQjIVN5JECreXIU/a3D8cFmmxfbqagjLQ1Svfp", "xP8pUw6EQllS31dm5r8/sT4Sl7v0xq3JXkV3CAr8kD33BDvqKZEe/Qq7Zwq518GS3tS3w4u8fpe0V2dFlu5I0W1mQsuZBT6HCDqXSIITGqh/5Pe2vuFTleSCuoD7OkelhFmZaHkmlS5M+B/fPgWbIw==");
            Scene scene9 = new Scene("TUOJvnGAXU/brQcDOKFfXRfqgkzx2n8Ye9ufy7DmIGsHr08IS0sur/Ao2hmMz2dL", "QpV0YUfpFv7VpmRCHa8HaGtB3dODZxZZpc48zQvuobvJEYBFlHcSr6QdhlNJnxmu/0eiIHuHsJuo2+NYKiAV/5UCjgVtQOt6indvz5KiERI=");
            Scene scene10 = new Scene("EUBWwUYyZnZnE4udIpQz3mFaQbmVnfErfYgfvILDX5ev5oT2hHS6kiJYELcMVOt/", "YOB7pEKDTpmN9CHLue04M1dn+2JdR2ECjTON24WJ9jKM2HOKDJoGCTx0DoXf23PdOFxDRZH9PoIDohr7JW3wMYCGEi/LIgoFTHSPVHAkZ9DLiZ2F1W21jQ2Urad7SJpFCZBrWfJTs9GYG8HYE4c2fjNsQkekEK29T1EzriCG/KiAt9+dIsQ2hHXjiFYRIN3h");
            scene1.addDecisions(new Decision[2]
            {
    new Decision("nzVO9dDwRv0ZD4ZTFLF7gQ==", Decision.Type.move, scene2),
    new Decision("zr0Xz0MSjyYRWaYy0GMPmw==", Decision.Type.move, scene3)
            });
            scene2.addDecisions(new Decision[2]
            {
    new Decision("vIqon9fBaDzEqnPt929ILA==", Decision.Type.input, scene4, "1D9MjS0NMgN2qoaagbb6ag=="),
    new Decision("5RZn8cZM0+AGsgjt9ljRcQ==", Decision.Type.move, scene1)
            });
            scene3.addDecisions(new Decision[2]
            {
    new Decision("tybxyUnWJWNd/XAjqMxPUQ==", Decision.Type.move, scene1),
    new Decision("FNkbBgiqaBw8ne1LnVImIw==", Decision.Type.move, scene3)
            });
            scene4.addDecisions(new Decision[1]
            {
    new Decision("IcIb5fDNucgr0olNiTwL6U/f/YmluvAmOBOJCXn4pVw=", Decision.Type.move, scene5)
            });
            scene5.addDecisions(new Decision[1]
            {
    new Decision("duZyjnd8KwR17K+UKADfkkwdxOAqRkMK0ZwDPHcshs4=", Decision.Type.move, scene6)
            });
            scene6.addDecisions(new Decision[1]
            {
    new Decision("3zbBBQGlbKX69VeVWoPxCw==", Decision.Type.combat, scene7, scene1_1)
            });
            scene7.addDecisions(new Decision[1]
            {
    new Decision("8oEJvy9PG/4UdblpWmDwaw==", Decision.Type.move, scene8)
            });
            scene1_1.addDecisions(new Decision[1]
            {
    new Decision("bJaNcHlTpVivIwXwyc2Wig==", Decision.Type.respawn, scene6)
            });
            scene9.addDecisions(new Decision[1]
            {
    new Decision("/nE1Xl1mCrp3nLHMuwcttZktXYvqz9BeBUn5ZUo2EK4=", Decision.Type.wait, scene10)
            });
            Program.scenes.Add(scene1);
            Program.scenes.Add(scene2);
            Program.scenes.Add(scene3);
            Program.scenes.Add(scene4);
            Program.scenes.Add(scene5);
            Program.scenes.Add(scene6);
            Program.scenes.Add(scene7);
            Program.scenes.Add(scene1_1);
            Program.scenes.Add(scene8);
            Program.scenes.Add(scene9);
            Program.scenes.Add(scene10);
            return scene1;
        }

        public static string Decrypt(string encryptedText)
        {
            byte[] buffer = Convert.FromBase64String(encryptedText);
            byte[] bytes = new Rfc2898DeriveBytes(Program.a, Encoding.ASCII.GetBytes(Program.b)).GetBytes(32);
            RijndaelManaged rijndaelManaged = new RijndaelManaged();
            rijndaelManaged.Mode = CipherMode.CBC;
            rijndaelManaged.Padding = PaddingMode.None;
            ICryptoTransform decryptor = rijndaelManaged.CreateDecryptor(bytes, Encoding.ASCII.GetBytes(Program.c));
            MemoryStream memoryStream = new MemoryStream(buffer);
            CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, decryptor, CryptoStreamMode.Read);
            byte[] numArray = new byte[buffer.Length];
            int count = cryptoStream.Read(numArray, 0, numArray.Length);
            memoryStream.Close();
            cryptoStream.Close();
            return Encoding.UTF8.GetString(numArray, 0, count).TrimEnd("\0".ToCharArray());
        }

        public static string Encrypt(string plainText)
        {
            byte[] bytes1 = Encoding.UTF8.GetBytes(plainText);
            byte[] bytes2 = new Rfc2898DeriveBytes(Program.a, Encoding.ASCII.GetBytes(Program.b)).GetBytes(32);
            RijndaelManaged rijndaelManaged = new RijndaelManaged();
            rijndaelManaged.Mode = CipherMode.CBC;
            rijndaelManaged.Padding = PaddingMode.Zeros;
            ICryptoTransform encryptor = rijndaelManaged.CreateEncryptor(bytes2, Encoding.ASCII.GetBytes(Program.c));
            byte[] array;
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, encryptor, CryptoStreamMode.Write))
                {
                    cryptoStream.Write(bytes1, 0, bytes1.Length);
                    cryptoStream.FlushFinalBlock();
                    array = memoryStream.ToArray();
                    cryptoStream.Close();
                }
                memoryStream.Close();
            }
            return Convert.ToBase64String(array);
        }
    }
}
