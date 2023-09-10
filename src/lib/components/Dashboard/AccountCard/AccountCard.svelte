<script>
  export let userImg = "/images/stock/photo-1534528741775-53994a69daeb.jpg";
</script>

<div
  class="bg-gray-200 py-[100px] rounded-xl flex flex-col items-center px-[150px] ml-[100px]"
>
  <div class="w-24 rounded-full">
    <img {userImg} alt="userImage" />
  </div>
  <h2 class="text-lg font-semibold mb-2 mt-10">Username</h2>
  <p>Level 1</p>
  <button class="btn btn-ghost mt-10">Log out</button>
</div>
