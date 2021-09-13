def print_general_info(player):
    print(f"""<General Info>
Player Speed: {player.speed}
Player Position: {player.pos}
Player Size: {player.size}
Player Aciton: {player.action}
Player On Ground: {player.on_ground}
Player Fall Time: {player.fall_time}
Player images idxs (idle, moving): {player.idle_img_idx}, {player.moving_img_idx}
Player Looking Left: {player.looking_left}

<Collision Info>
Colision Box Pos: {player.colide_pos}
Colision Box Size: {player.colide_size}



    """)