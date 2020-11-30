using System;
using System.Threading;

namespace Nigeria
{
    internal class Scene
    {
        private string label;
        private Decision[] decisions;
        public string uuid;

        public Scene(string uuid, string label)
        {
            this.label = label;
            this.uuid = uuid;
            Console.WriteLine(Program.Decrypt(label));
        }

        public void addDecisions(Decision[] decisions)
        {
            this.decisions = decisions;
        }

        public void start()
        {
            Console.Clear();
            Program.currentScene = this;
            Program.SaveGame();
            Console.WriteLine(Program.Decrypt("oMkOQXvm8714CxH6edlvOg==") + (object)Program.playerHealth);
            if (Program.iscombat)
                Console.WriteLine(Program.Decrypt("1CKtcDok5o5kCmEXzzO5iQ==") + (object)Program.monsterHealth);
            Console.WriteLine(Program.Decrypt(this.label));
            Console.WriteLine();
            if (this.decisions != null)
            {
                for (int index = 0; index < this.decisions.Length; ++index)
                    Console.WriteLine("[" + (object)(index + 1) + "] " + Program.Decrypt(this.decisions[index].label));
            }
            Console.WriteLine();
            Console.Write(Program.Decrypt("xb2BEku2fQOgh6bRs/hBbA=="));
            int result = 0;
            bool flag = false;
            while (!flag)
            {
                flag = int.TryParse(Console.ReadLine(), out result);
                if (this.decisions == null || flag && (result < 1 || result > this.decisions.Length))
                    flag = false;
                if (!flag)
                {
                    Console.WriteLine(Program.Decrypt("vnwLTi4QrLhAJr2DTzCh4r8LS71fOEfbI6NFeoOhyWM="));
                    Console.Write(Program.Decrypt("xb2BEku2fQOgh6bRs/hBbA=="));
                }
                else
                    --result;
            }
            if (this.decisions[result].type == Decision.Type.move)
            {
                Program.iscombat = false;
                this.decisions[result].scene.start();
            }
            else if (this.decisions[result].type == Decision.Type.input)
            {
                Program.iscombat = false;
                Console.WriteLine();
                Console.Write(Program.Decrypt("e6E/nSOvPoSlVdVa+o6wjg=="));
                if (Console.ReadLine().Trim().ToLower() == Program.Decrypt(this.decisions[result].value))
                {
                    this.decisions[result].scene.start();
                }
                else
                {
                    Console.WriteLine(Program.Decrypt("jpX9tDoKLJQKP1ncnS6FfQHV0XTaNPVQ6ACBb3r2Q8trwpPUnqeI+tWoXufPrST0"));
                    Console.ReadLine();
                    this.start();
                }
            }
            else if (this.decisions[result].type == Decision.Type.combat)
            {
                Program.iscombat = true;
                --Program.playerHealth;
                --Program.monsterHealth;
                if (Program.playerHealth <= 0)
                    this.decisions[result].scene1.start();
                else if (Program.monsterHealth <= 0)
                    this.decisions[result].scene.start();
                else
                    this.start();
            }
            else if (this.decisions[result].type == Decision.Type.wait)
            {
                int tickCount = Environment.TickCount;
                do
                {
                    Thread.Sleep(1000);
                    Console.Clear();
                    Console.WriteLine(Program.Decrypt("iCk3E5ONh47yoqY2u+uSAljEu0WqY8y4XnFzxkbS46QVcA0tzWOSQg/tf3vR9quR") + (object)(3000 - (Environment.TickCount - tickCount) / 1000) + Program.Decrypt("xwfhXKyCA87FJzXi6AOuMQ=="));
                }
                while (3000000 - Environment.TickCount + tickCount >= 0);
                this.decisions[result].scene.start();
            }
            else
            {
                if (this.decisions[result].type != Decision.Type.respawn)
                    return;
                Program.iscombat = false;
                Program.monsterHealth = 20;
                Program.playerHealth = 10;
                this.decisions[result].scene.start();
            }
        }
    }
}
